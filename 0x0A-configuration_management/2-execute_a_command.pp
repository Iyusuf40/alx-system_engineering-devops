# manifest kills killmenow process

exec { 'kill killmenow':
  command => '/bin/pkill killmenow',
}
