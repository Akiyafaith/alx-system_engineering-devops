#fix a bug  using puppet

exec {'fix-wordpress bug':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
