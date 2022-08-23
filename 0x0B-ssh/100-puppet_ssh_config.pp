# Client configuration file with Puppet.

file { '/etc/ssh/ssh_config':
  ensure => 'present',
}

exec { 'Identity'
    command => '/usr/bin/echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}

exec { 'No password login'
    command => '/usr/bin/echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
