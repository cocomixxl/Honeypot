# Honeypot Attack Findings  
*Last Updated: 2025-4-2*  

## Executive Summary  
| Metric               | Count     | Top Target          |
|----------------------|-----------|---------------------|
| Total Attacks        | 880    | SSH (Port 2222)     |
| Unique Attackers     | 72     | HTTP (Port 80)      |
| Data Collected       | | Telnet (Port 23)    |

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
soon
```
**CyberChef Steps:**
# Kibana Dashboards
**Most Targeted Ports**
**Attack Timeline**
```
soon
```
# Spiderfoot Intel
| IP              | Blacklist     | Associated Malware         |
|----------------------|-----------|---------------------|
|         |     |      |
|     |     |    |

# Security Recommendations
