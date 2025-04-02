**Purpose**: Capture and analyze attacker behavior in a controlled environment.  
**Host OS**: Ubuntu Server 22.04 LTS (minimal install).  
**Virtualization**: Digital ocean Droplet.  
**Network**: Dedicated VPC for honeypot traffic.  
1. **Firewall Rules**:  
   - Allow inbound: TCP 80,443,22 (honeypot ports).  
   - Deny all outbound from honeypots (except ELK logging).  
   - SSH restricted  

2. **IP Addressing**:  
   - Host  
   - Docker Subnet
# Security measures
- **No Internet Access**: Honeypots run in an internal Docker network.  
- **Anonymization**: Logs sanitized.  
- **Automated Updates**: Daily cron jobs for `apt-get update`.  
