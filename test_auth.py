from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
from openai import OpenAI
import _keys

print("1. Testing Azure Connection...")
try:
    LogsQueryClient(DefaultAzureCredential())
    print("✅ Azure authentication successful!")
except Exception as e:
    print(f" ❌ Azure failed: {e}")

print("\n2. Testing OpenAI connection...")
try:
    client = OpenAI(api_key=_keys.OPEN_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say 'OpenAI connection successful!'"}],
        max_tokens=20
    )
    print("   ✅ OpenAI key valid!")
    print(f" Response: {response.choices[0].message.content}")
except Exception as e:
    print(f" ❌ OpenAI failed: {e}")