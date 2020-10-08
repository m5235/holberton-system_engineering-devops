# Puppet script
exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { 'service nginx restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
 }
