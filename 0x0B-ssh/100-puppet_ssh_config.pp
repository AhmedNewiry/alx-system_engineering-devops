#practice puppet by making changes to ssh_config file
file_line { 'IdentifyFile property':
	ensure => 'present',
	path => '/etc/ssh/ssh_config',
	replace => 'true'
	line => '	IdentifyFile ~/.ssh/school'
}

file_line { 'PasswordAuthentication property':
	ensure => 'present',
	path => '/etc/ssh/ssh_config',
	replace => 'true'
	line => '	PasswordAuthentication no'
}
