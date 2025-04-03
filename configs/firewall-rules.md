# Firewall Configuration for T-Pot Honeypot  
*Protecting the host while exposing honeypot services*  

## DigitalOcean Cloud Firewall Rules  
*(Network-level protection via DO dashboard)*  

### **Inbound Rules**  
| Purpose          | Protocol | Port    | Source          | Action |  
|------------------|----------|---------|-----------------|--------|  
| SSH Management   | TCP      | 22      | `my IP`  | ALLOW  |  
| T-Pot Web UI     | TCP      | 64297   | Any             | ALLOW  |  
| Cowrie (SSH)     | TCP      | 2222    | Any             | ALLOW  |  
| Glastopf (HTTP)  | TCP      | 80,443  | Any             | ALLOW  |  
| **All other**    | Any      | Any     | Any             | DENY   |  

### **Outbound Rules**  
| Purpose          | Protocol | Port    | Destination     | Action |  
|------------------|----------|---------|-----------------|--------|  
| Updates/Logging  | TCP/UDP  | Any     | Any             | ALLOW  |  

---

## Host Firewall (UFW) Rules  
*(Extra hardening on the droplet itself)*  

```bash
# Reset and default deny
sudo ufw reset
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow ONLY honeypot ports
sudo ufw allow from My IP to any port 22 proto tcp         # SSH
sudo ufw allow 64297/tcp                                   # T-Pot Web
sudo ufw allow 2222/tcp                                    # Cowrie
sudo ufw allow 80,443/tcp                                  # Glastopf

# Block Docker outbound (prevent accidental malware calls)
sudo ufw deny out from 172.18.0.0/16 to any

# Enable
sudo ufw enable
sudo ufw status verbose
