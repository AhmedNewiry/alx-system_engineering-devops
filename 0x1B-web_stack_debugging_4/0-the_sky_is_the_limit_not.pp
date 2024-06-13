exec { 'increase worker limit':
  command     => 'sed -i "s/4/4000/" /etc/default/nginx && systemctl restart nginx',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  logoutput   => true,
  unless      => 'grep -q "4" /etc/default/nginx',
}
