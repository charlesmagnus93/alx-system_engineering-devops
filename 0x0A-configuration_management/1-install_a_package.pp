# install package flask

package { 'flask':
  provider => 'pip',
  ensure   => '2.1.0',
}
