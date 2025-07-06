import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

print(f"🔎 JIRA_DOMAIN: {JIRA_DOMAIN}, JIRA_EMAIL: {JIRA_EMAIL}, JIRA_PROJECT_KEY: {JIRA_PROJECT_KEY}")
def create_jira_issue(summary: str, description: str):
    url = f"https://{JIRA_DOMAIN}/rest/api/2/issue"
    headers = {
        "Content-Type": "application/json"
    }
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"}
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers, auth=auth)

        print(f"📤 Payload: {payload}")
        print(f"📥 Status: {response.status_code}")
        print(f"📥 Response: {response.text}")

        if response.status_code == 201:
            issue_key = response.json()["key"]
            print(f"✅ JIRA Issue Created: {issue_key}")
            return issue_key
        else:
            print(f"❌ JIRA Issue Creation Failed with status {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Exception occurred while creating JIRA: {e}")
        return None

