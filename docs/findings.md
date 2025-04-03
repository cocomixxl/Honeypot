# Honeypot Attack Findings  
*Last Updated: 2025-4-3*  

## Executive Summary  
| Metric               | Count     | Top Target          |
|----------------------|-----------|---------------------|
| Total Attacks        | 880    | SSH (Port 2222)     |
| Unique Attackers     | 72     | HTTP (Port 80)      |
| Data Collected       | 13.1 kb| Telnet (Port 23)    |

---

## Attack Map Insights  

- **Top 3 Attack Sources**:  
  1. United States (29%)  
  2. Kazahkstan (28%)  
  3. Netherlands (12%)  
- **Notable Cluster**: Spike in scans from Kazahkstan (ASN 	JSC Kazakhtelecom).  

---

##  Top Attack Patterns  
### 1. 

Top Username: root (89% of attempts)

Common Passwords: admin, 123456, password
## 2. Web Exploits 
**Decoded Payload (CyberChef):**
Analysis:
```
GET /wp-admin/wp-json/wp/v2/users/?_fields=id,username HTTP/1.1  .
```
# Payload Deep Dive
Case Study: Base64-Obfuscated Attack
**Raw Log:**
```
UE9TVCAvaXBwIEhUVFAvMS4xDQpIb3N0OiAxNDMuMTEwLjIyMS45MDo2MzENClVzZXItQWdlbnQ6IE1vemlsbGEvNS4wIHpncmFiLzAueA0KQ29udGVudC1MZW5ndGg6IDE0Nw0KQWNjZXB0OiAqLyoNCkNvbnRlbnQtVHlwZTogYXBwbGljYXRpb24vaXBwDQpBY2NlcHQtRW5jb2Rpbmc6IGd6aXANCg0KAgEACwAAAAEBRwASYXR0cmlidXRlcy1jaGFyc2V0AAV1dGYtOEgAG2F0dHJpYnV0ZXMtbmF0dXJhbC1sYW5ndWFnZQAFZW4tdXNFAAtwcmludGVyLXVyaQAcaXBwOi8vMTQzLjExMC4yMjEuOTA6NjMxL2lwcEQAFHJlcXVlc3RlZC1hdHRyaWJ1dGVzAANhbGwD
```
**CyberChef Steps:**
- Magic operation to know the kind of payload then use the right operation wich was from base64\
POST /ipp HTTP/1.1\
Host: 143.110.221.90:631\
User-Agent: Mozilla/5.0 zgrab/0.x\
Content-Length: 147\
Accept: */*\
Content-Type: applica\tion/ipp\
Accept-Encoding: gzip</h>\

# Kibana Dashboards
**Most Targeted Ports**
445 SMB exploitation attempts
**Attack Timeline**
```
Peak Hours: 11:00-13:00 EST (Automated bots)
```
