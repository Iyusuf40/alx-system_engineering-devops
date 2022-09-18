# configures /etc/ssh/ssh_config
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "Host *
	PasswordAuthentication no
	IdentityFile ~/.ssh/school",
}
