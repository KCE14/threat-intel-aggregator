#!/usr/bin/env python3

"""
Threat Intel Aggregator - Main CLI
"""

import sys
from api_clients import check_abuseipdb
from utils import format_results_as_yaml, output_yaml

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    save_file = '--save' in sys.argv
    print(f"🔍 Checking: {ip_address}")
    
    # Query AbuseIPDB
    print("\n 📡 Querying AbuseIPDB...")
    result = check_abuseipdb(ip_address)

    if result:
        formatted = format_results_as_yaml(ip_address, result)
        output_yaml(formatted, save_to_file=save_file)
    else:
        print("❌ Failed to get results")

if __name__ == "__main__":
    main()