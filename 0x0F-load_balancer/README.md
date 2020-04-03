#0x0F. Load balancer
---
Let’s improve our web stack so that there is redundancy for our web servers. 
This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. 
If one web server fails, we will still have a second one to handle requests.
For this project, you will need to write Bash scripts to automate your work. 
All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.
---
| File | Description |
| --- | --- |
| [0-custom_http_response-header]()|  Bash script that configures a brand new Ubuntu machine, so that its HTTP response contains a custom header, with the name of the custom HTTP header being X-Served-By and finally with the value of the custom HTTP header with the hostname of the server Nginx is running on. |
| [1-install_load_balancer]() | Bash script that configures a new Ubuntu machine with HAproxy with version equal or greater than 1.5 so that it send traffic to web-01 and web-02 and distributes requests using a roundrobin algorithm.|
