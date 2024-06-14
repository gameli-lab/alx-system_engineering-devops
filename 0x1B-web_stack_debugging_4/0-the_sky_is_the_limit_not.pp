# Increases ULIMIT value to 4096

exec { 'fix--for-nginx':
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 4096\\\"/' \
/etc/default/nginx; service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}
