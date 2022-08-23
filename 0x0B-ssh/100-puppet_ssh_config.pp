# Client configuration file with Puppet.

file_line {'disable password login':
    ensure => 'absent',
    line   => 'PasswordAuthentication no',
    path   => '~/.ssh/school',
}