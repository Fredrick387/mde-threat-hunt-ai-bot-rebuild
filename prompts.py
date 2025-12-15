TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "plan_log_query",
            "description": "Choose the best Log Analytics table and parameters for the user's threat hunting request",
            "parameters" : {
                        "type": "object",
                        "properties": {
                                "table_name": {
                                    "type": "string",
                                    "enum": [
                                        "DeviceLogonEvents",
                                        "SigninLogs",
                                        "DeviceNetworkEvents",
                                        "DeviceProcessEvents",
                                        "AzureActivity"
                                    ],
                                    "description": "The Log Analytics table that contains relevant data"
                                },
                            "time_range_hours": {
                                "type": "integer",
                                "description": "How many hours back to search from now"
                            },
                            "device_name": {
                                "type": "string",
                                "description": "Specific device name if mentioned in the request (e.g., windows-target-1)"
                            },
                            "user_principal_name": {
                                "type": "string",
                                "description": "specific user if mentioned (Azure AD UPN)"
                            },
                            "fields": {
                                "type": "array",
                                "items": {"type": "string"},
                             "description": "The minimal list of fields needed to investigate the hunt"
                            }
                        
                        },
                        "required": ["table_name", "time_range_hours", "fields"]
            }
        }
    }
]
SYSTEM_PROMPT_PLANNING = {
    "role": "system",
    "content": (
        "You are an elite SOC analyst specialized in Microsoft Defender for Endpoint and Azure AD logs."
        "Your job is to translate the user's natural-language threat hunting request into a precise query plan."
        "Always choose the single most releveant table from the allowed list."
        "Only include device_name or user_principal_name if the user explicitly mentions a specific device or user."
        "Select the absolute minimal set of fields needed to investitage the request."
        "Be Conservative and accurate - never guess"
    )
}