# Client configuration file with Puppet.

exec { 'Configuration to refuse to authenticate using a password':
    command  => 'eval $(ssh-agent) && ssh-add',
    provider => 'shell',
}
