# Client configuration file with Puppet.

file_line {'disable password login':
    path => '/etc/ssh/sshd_config',
    line => ' PasswordAuthentication no',
    ensure => 'present',
}
