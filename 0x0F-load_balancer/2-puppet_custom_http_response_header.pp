# puppet sets up an nginx server in an ubuntu env
package {  'nginx':
  ensure => installed,
}

service {  'nginx':
  ensure  => running,
  require => [ Package['nginx'],
  File['/var/www/html/index.html'],
  Exec['configure nginx'] ],
}

file {  '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

exec {  'configure nginx':
  command => '/bin/sed -i "s/server_name _;/server_name _;\n\trewrite \
^\/redirect_me https:\/\/www.digitalocean.com\/community\/tutorials\
\/how-to-create-temporary-and-permanent-redirects-with-nginx permanent;/" \
/etc/nginx/sites-available/default',
  require => Package['nginx'],
}

exec {  'add header' :
  command => '/bin/sed -i "s/listen 80 default_server;/listen 80 default_server;\n\t\
add_header X-Served-By $(hostname);/" /etc/nginx/sites-enabled/default',
  require => Exec['configure nginx'],
}
