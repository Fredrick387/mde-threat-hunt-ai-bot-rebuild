import json
from executor import get_query_context, query_logs

print("=== MDE Threat Hunt AI Bot - Query Planner ===")
print("You are now talking to an AI SOC analyst with real log access. \n")



# Step 1: Get the user's natural-language hunt request
user_input = input("Hunt request: ")

# Step 2: Generate the Structured plan
print("\nGenerating Query Plan...")
plan = get_query_context(user_input)


print("\n" + "="*60)
print("GENERATED QUERY PLAN")
print("="*60)
print(json.dumps(plan, indent=2))
print("="*60)

# Step 3: Execute the plan against real logs
print("\nQuerying Log Analytics Workspace...")
results = query_logs(plan)

# Step 4: Display results
if results is not None:
    print("\n" + "="*60)
    print("QUERY RESULTS")
    print("="*60)
    print(results.to_string(index=False))
    print(f"\nTotal records returned: {len(results)}")
else:
    print("\nNo matching records found in the workspace")