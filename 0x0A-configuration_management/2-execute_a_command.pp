# executes a command
exec {'killmenow':
command => 'pkill --signal SIGTERM killmenow',
path    => '/usr/bin'
}
