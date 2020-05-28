# Debugging
exec { 'process':
  command  => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/nginx.conf && sudo service nginx restart",
  provider => 'shell',
}
