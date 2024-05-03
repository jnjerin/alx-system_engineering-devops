# Kill a process
exec { 'kill_killmenow_process':
  command   => '/usr/bin/pkill -f "killmenow"',
  provider      => 'shell',
  refreshonly => true,
}