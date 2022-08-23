# Client configuration file with Puppet.

file { '/etc/ssh/sshd_config':
  ensure => 'present',
}

exec { 'Identity'
    command => 'echo ssh -i ~/.ssh/school > /etc/ssh/ssh_config'
}

exec { 'No password login'
    command => 'echo PasswordAuthentication no > /etc/ssh/ssh_config'
}
