# fix 500 error

exec { 'fix bug':
  path    =>  '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ,
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  onlyif  => 'test -e /var/www/html/wp-settings.php',
  
}
