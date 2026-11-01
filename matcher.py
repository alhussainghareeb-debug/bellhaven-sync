import json
import requests

API_TOKEN = "bh_P2Lz48fRF1VSQgNjk0t00g"
BASE_URL = "https://analyst-assessment-production.up.railway.app/api/v1"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}


def get_all_crm_accounts():
  print("Fetching all CRM accounts...")
  response = requests.get(f"{BASE_URL}/accounts?page_size=200", headers=HEADERS)
  if response.status_code == 200:
    res_json = response.json()
    accounts = res_json.get("data", [])
    print(f"Successfully fetched {len(accounts)} CRM accounts!")
    return accounts
  else:
    print(f"Failed: {response.status_code}")
    return []


if __name__ == "__main__":
  accounts = get_all_crm_accounts()
  if accounts:
    print(f"\nTotal accounts loaded: {len(accounts)}")
    # Save locally so we can build our review interface next
    with open("crm_accounts.json", "w") as f:
      json.dump(accounts, f, indent=4)
    print("Saved to crm_accounts.json successfully!")