# Install a package
package { 'flask-2.1.0':
  ensure   => '2.1.0',
  name     => 'flask'
  provider => 'pip3',
}