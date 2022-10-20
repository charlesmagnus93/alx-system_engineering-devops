# Kills a process by name

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
