# Executing a command with Puppet.

exec { 'Killing a process named killmenow':
    command  => 'pkill -f 'killmenow'',
    provider => 'shell',
    onlyif   => '/usr/bin/killmenow -e /home/devpacho/HOLBERTON/holbertonschool-system_engineering-devops/0x0A-configuration_management/killmenow',
}
