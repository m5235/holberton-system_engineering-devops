# fix 500 error

exec { 'fix debug':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    =>  '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ,
  
}
