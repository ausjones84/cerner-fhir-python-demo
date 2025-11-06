import os
from pathlib import Path
import requests
from dotenv import load_dotenv

# 1) force-load .env from the same folder as this file
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

print("✅ Loaded .env from:", env_path)

# 2) read values
token_url = os.getenv("CERNER_TOKEN_URL")
fhir_base = os.getenv("CERNER_FHIR_BASE")
client_id = os.getenv("CERNER_CLIENT_ID")
client_secret = os.getenv("CERNER_CLIENT_SECRET")
scope = os.getenv("CERNER_SCOPE")

print("Token URL:", token_url)
print("FHIR Base:", fhir_base)
print("Client ID:", client_id)
print("Scope:", scope)

# 3) stop early if env isn't filled in yet
missing = [name for name, val in {
    "CERNER_TOKEN_URL": token_url,
    "CERNER_FHIR_BASE": fhir_base,
    "CERNER_CLIENT_ID": client_id,
    "CERNER_CLIENT_SECRET": client_secret,
    "CERNER_SCOPE": scope,
}.items() if not val]

if missing:
    print("\n⚠️ Missing values in .env:", ", ".join(missing))
    print("Fill them in and run again.")
else:
    # 4) try calling Cerner token endpoint
    try:
        resp = requests.post(token_url, data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": scope,
        })
        print("\nAuth status:", resp.status_code)
        print(resp.text)
    except Exception as e:
        print("\n⚠️ Error connecting:", e)

print("\n--- Demo Completed ---")

