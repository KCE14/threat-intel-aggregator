"""
API clients for threat intelligence services
"""

import requests
import yaml

def load_config():
    """Load API keys from config.yaml"""
    with open('config/config.yaml', 'r') as f:
        return yaml.safe_load(f)
    
def check_abuseipdb(ip_address):
    """
    Query AbuseIPDB for IP reputation
    Returns: dict with results or None if error
    """

    config = load_config()
    api_key = config['api_keys']['abuseipdb']

    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        print(f"DEBUG: Status code: {response.status_code}")
        print(f"DEBUG: Response: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error querying AbuseIPDB: {e}")
        return None