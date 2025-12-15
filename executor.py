import json
from openai import OpenAI
import _keys
from prompts import TOOLS, SYSTEM_PROMPT_PLANNING

from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
from datetime import timedelta
import pandas as pd

# Create Azure Log Analytics Client
logs_client = LogsQueryClient(DefaultAzureCredential())

def query_logs(plan: dict):
    """
    Execute the GPT-generated queary plan agaisnt Log Analystics and return results
    """
    workspace_id = _keys.LOG_ANALYTICS_WORKSPACE_ID 

    # Start building the KQL Query
    kql = f"{plan['table_name']}"

    # Add time filter (always required)
    kql += f"\n| where TimeGenerated > ago({plan['time_range_hours']}h)"

    # Add device filter if specified
    if plan.get("device_name"):
        kql += f"\n | where DeviceName =~ '{plan['device_name']}'"
    
    if plan.get("user_principal_name"):
        kql += f"\n| where UserPrincipalName =~ '{plan['user_principal_name']}"
    
    # Project only the fields we need
    fields_list = ", ".join(plan["fields"])
    kql += f"\n| project {fields_list}"

    # Optional: sory by time descending for readability
    kql += "\n| order by TimeGenerated desc"

    print("\nExecuting KQL query:")
    print(kql)
    print("-" * 50)
    
    # Execute the query against Log Analytics
    response = logs_client.query_workspace(
        workspace_id=workspace_id,
        query=kql,
        timespan=timedelta(hours=plan["time_range_hours"])
    )

    # Check if we got any results
    if not response.tables or len(response.tables[0].rows) == 0:
        print("No Records Returned")
        return None
    
    # Convert to pandas DataFrame for nice display
    table = response.tables[0]
    columns = [col.name for col in table.columns]
    df = pd.DataFrame(table.rows, columns=columns)

    print(f"Retrieved {len(df)} records")
    return df


    



# Create the OpenAI client using your key
client = OpenAI(api_key=_keys.OPEN_API_KEY)

def get_query_context(user_query: str):
    """
    Send the user's natural -language request to OpenAI and get back a structured query plan
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            SYSTEM_PROMPT_PLANNING,                     # The Elite SOC Analyst Instructions
            {"role": "user", "content": user_query}     # What the user actually typed
        ],
        tools=TOOLS,                                    # Our function definition
        tool_choice="required"                          # Force GPT to use our tool
    )

# Extract the tool call arguments that GPT returned  
    tool_call = response.choices[0].message.tool_calls[0]
    arguments_json = tool_call.function.arguments

# Convert the JSON string to a real Python dictionary
    query_plan = json.loads(arguments_json)

    return query_plan