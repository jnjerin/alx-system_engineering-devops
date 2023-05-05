# 0x10-https_ssl

This project explores the concept of securing website traffic.

* **0-world_wide_web** - Configures domain and displays info about subdomains.
* **1-haproxy_ssl_termination** - Terminating SSL on HAproxy. This means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.
* **100-redirect_http_to_https** - Configures HAproxy to automatically redirect HTTP traffic to HTTPS so that no unencrypted traffic is possible. 
