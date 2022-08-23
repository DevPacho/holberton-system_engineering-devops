# Client configuration file with Puppet.

file_line {'disable password login':
    ensure => 'absent',
    line   => 'PasswordAuthentication yes',
    path   => '/etc/ssh/sshd_config',
}