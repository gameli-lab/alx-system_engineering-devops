# Using puppet to edit ssh config file

file { 'etc/ssh/sshd_config':
ensure	=> present,
}

augeas { 'Turn off password authentication':
  context => '/files/etc/ssh/sshd_config',
  changes => [
    'set PermitRootLogin no',
  ],
  require => File['/etc/ssh/sshd_config'],
}

augeas { 'Declare identity file':
  context => '/files/etc/ssh/sshd_config',
  changes => [
    'set IdentityFile ~/.ssh/school',
  ],
  require => File['/etc/ssh/sshd_config'],
}

service { 'sshd':
  ensure => running,
  enable => true,
}

