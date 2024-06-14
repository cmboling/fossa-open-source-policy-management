import os
import yaml
import requests
from pathlib import Path

def load_policy(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def update_fossa_policy(policy, access_token, policy_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}',
    }
    url = f'https://app.fossa.com/api/policies/{policy_id}/rules'

    for section in ['approved_license', 'flagged_license', 'denied_license']:
        for rule in policy.get(section, []):
            rule_data = {
                'licenseId': rule['licenseId'],
                'type': rule['type'],
                'notes': rule.get('notes', ''),
                'nameCondition': rule.get('nameCondition'),
                'depthCondition': rule.get('depthCondition'),
                'linkingCondition': rule.get('linkingCondition')
            }
            response = requests.post(url, headers=headers, json=rule_data)
            if response.status_code != 200:
                print(f"Failed to update license {rule['licenseId']} in FOSSA: {response.text}")

def main():
    policy_files = os.getenv('CHANGED_POLICY_FILES').split()
    access_token = os.getenv('FOSSA_FULL_ACCESS_TOKEN')
    
    for policy_file in policy_files:
        policy = load_policy(policy_file)
        policy_id = policy['workflow-field-policy-id']
        update_fossa_policy(policy, access_token, policy_id)

if __name__ == '__main__':
    main()
