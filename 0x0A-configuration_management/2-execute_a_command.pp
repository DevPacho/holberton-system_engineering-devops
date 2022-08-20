# Executing a command with Puppet.

exec { 'Killing a process named killmenow':
    command  => 'pkill -f 'killmenow'',
    provider => 'shell',
}
