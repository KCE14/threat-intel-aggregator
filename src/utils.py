"""
Utility functions for printing YAML output
"""
import yaml
from datetime import datetime

def format_results_as_yaml(ip_address, abuseipdb_data):
    """
    Take raw API response and structure it for YAML output
    """
    data = abuseipdb_data.get('data', {})

    results = {
        'scan_info': {
            'ip_address': ip_address,
            'scan_time': datetime.now().isoformat(),
            'tool': 'Threat Intel Aggregator'
        },
        'abuseipdb': {
            'abuse_score': data.get('abuseConfidenceScore'),
            'total_reports': data.get('totalReports'),
            'last_reported': data.get('lastReportedAt'),
            'isp': data.get('isp'),
            'domain': data.get('domain'),
            'country_code': data.get('countryCode'),
            'is_tor': data.get('isTor'),
            'is_public': data.get('isPublic')
        }
    }
    
    return results

def output_yaml(results, save_to_file=False, output_dir='output'):
    """
    Print YAML to console and optionally save to file
    """
    yaml_string = yaml.dump(results, default_flow_style=False, sort_keys=False)

    print("\n📄 YAML Output:")
    print("-" * 40)
    print(yaml_string)

    if save_to_file:
        import os
        os.makedirs(output_dir, exist_ok=True)

        ip = results['scan_info']['ip_address']
        filename = f"{output_dir}/{ip}_report.yaml"

        with open(filename, 'w') as f:
            f.write(yaml_string)

        print(f"💾 Saved to: {filename}")

    return yaml_string