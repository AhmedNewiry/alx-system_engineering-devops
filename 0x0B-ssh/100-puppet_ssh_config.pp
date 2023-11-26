#practice puppet by making changes to ssh_config file
file_line { 'IdentifyFile property':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentifyFile ~/.ssh/school',
  replace => 'true',

}

file_line { 'PasswordAuthentication property':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  replace => 'true',
  line    => '	PasswordAuthentication no',
  replace => 'true',

}
