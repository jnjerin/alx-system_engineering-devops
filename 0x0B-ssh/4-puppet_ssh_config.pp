file { '~/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => '
    Host 52.3.241.110
            IdentityFile ~/.ssh/school
            PreferredAuthentications publickey
            PasswordAuthentication no
  ',
}
