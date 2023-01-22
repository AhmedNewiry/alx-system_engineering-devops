# creating a custom HTTP header response with Puppet.
exec { 'custom header':
  command  => 'apt-get -y update;
  sudo apt-get -y install nginx;
  sudo sed -i "/server_name _;$/a add_header X-Served-By $hostname;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
