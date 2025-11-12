#!/usr/bin/env python3

"""
Threat Intel Aggregator - Main CLI
"""

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    print(f"🔍 Checking: {ip_address}")
    # TODO: Add API calls here

if __name__ == "__main__":
    main()