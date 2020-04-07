#0x10. HTTPS SSL
---
- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means
---
| File | Description |
| --- | --- |
| [0-https_abc]() | Answers to the questionare. |
| [1-world_wide_web]() |Configure the domain zone so that the subdomain www points to the load-balancer IP. |
| [2-haproxy_ssl_termination]() | Creates a certificate using certbot and configure HAproxy to accept encrypted traffic for the subdomain www.|
| [ 100-redirect_http_to_https]() | HAproxy configuration to automatically redirect HTTP traffic to HTTPS. |

