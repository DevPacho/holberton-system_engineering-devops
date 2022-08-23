# Client configuration file with Puppet.

file { '/etc/ssh/ssh_config':
  ensure => present,
}
-> exec { 'Adding -i flag':
  command  => '/usr/bin/echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
-> exec { 'Adding no password in login':
  command  => '/usr/bin/echo "PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
