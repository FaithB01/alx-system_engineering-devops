# Fix a typo within wp-settings.php
exec { 'fix-wordpress':
  command => '/bin/sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
}
