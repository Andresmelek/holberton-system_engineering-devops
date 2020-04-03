#same as 0 but with puppet
exec { 'add_header':
  command  => "apt-get update && apt-get -y install nginx && sed -i '/listen 80 default_server;/a && sed -i '22i add_header X-Served-By $hostname;' /etc/nginx/nginx.conf && service nginx start",
  provider => 'shell',
}
