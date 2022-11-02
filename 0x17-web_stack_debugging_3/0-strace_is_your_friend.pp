# puppet manifest ensuring file /var/www/html/index.html exists

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Gotcha',
}
