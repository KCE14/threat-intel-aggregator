#!/usr/bin/env python3

"""
Threat Intel Aggregator - Main CLI
"""

import sys
from api_clients import check_abuseipdb

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    print(f"🔍 Checking: {ip_address}")
    
    # Query AbuseIPDB
    print("\n 📡 Querying AbuseIPDB...")
    result = check_abuseipdb(ip_address)

    if result:
        data = result.get('data', {})
        print(f"\n✅ Results:")
        print(f"    IP: {data.get('ipAddress')}")
        print(f"    Abuse Score {data.get('abuseConfidenceScore')}/100")
        print(f"    Total Reports: {data.get('totalReports')}")
        print(f"    Last Reported: {data.get('lastReportedAt', 'Never')}")
    else:
        print("❌ Failed to get results")

if __name__ == "__main__":
    main()