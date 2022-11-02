# puppet manifest ensuring file /var/www/html/index.html exists
file { '/var/www/html/index.php':
  ensure  => present,
  replace => true,
  content => '<?php
echo "Holberton";
?>',
}

