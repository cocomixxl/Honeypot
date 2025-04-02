# 🕵️‍♂️ Honeypot Attack Findings  
*Last Updated: $(date +%Y-%m-%d)*  

## 📌 Executive Summary  
| Metric               | Count     | Top Target          |
|----------------------|-----------|---------------------|
| Total Attacks        | 12,742    | SSH (Port 2222)     |
| Unique Attackers     | 1,642     | HTTP (Port 80)      |
| Data Collected       | 14.2 GB   | Telnet (Port 23)    |

---

## 🌍 Attack Map Insights  

- **Top 3 Attack Sources**:  
  1. United States (29%)  
  2. Kazahkstan (28%)  
  3. Netherlands (12%)  
- **Notable Cluster**: Spike in scans from Netherlands (ASN 12345).  

---

## 🔥 Top Attack Patterns  
### 1. SSH Bruteforce (Cowrie)  
```json
// Sample Kibana Query  
{
  "query": { "match": { "eventid": "cowrie.login" } },
  "size": 0,
  "aggs": { "top_passwords": { "terms": { "field": "password" } } }
}
