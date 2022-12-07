# Uses pkill to kill a process named 'killmenow'
exec { 'process killer':
  command => 'pkill -f "killmenow"',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => ''
}
