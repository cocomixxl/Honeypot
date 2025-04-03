#!/usr/bin/env python3
""" Extracts brute-force attempts & payloads"""

import json
import sys
from collections import defaultdict

# Initialize storage for attack statistics
stats = {
    'ips': defaultdict(int),      # Tracks attacker IPs and their frequencies
    'creds': defaultdict(int)     # Stores username:password combinations
}

# Open and read the Cowrie honeypot log file
with open(sys.argv[1]) as f:      # Takes log file path as command-line argument
    for line in f:                # Processes each log entry line-by-line
        log = json.loads(line)    # Parses JSON-formatted log entry

        # Detect SSH/Telnet login attempts
        if log.get('eventid') == 'cowrie.login':
            stats['ips'][log['src_ip']] += 1                     # Count IP occurrences
            stats['creds'][f"{log['username']}:{log['password']}"] += 1  # Track credentials

# Generate summary report
print(json.dumps({
    'top_ips': sorted(
        stats['ips'].items(), 
        key=lambda x: -x[1]       # Sort IPs by attack count (descending)
    )[:3],                        # Show top 3 attackers
    'top_creds': sorted(
        stats['creds'].items(), 
        key=lambda x: -x[1]       # Sort creds by usage frequency
    )[:2]                         # Show top 2 credential pairs
}, indent=2))                     # Pretty-print JSON output
