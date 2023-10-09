# sets up your web servers for the deployment of web_static
exec { 'update':
  provider => shell,
  command  => 'sudo apt -y update',
  before   => Exec['install nginx']
}
exec { 'install nginx':
  provider => shell,
  command  => 'sudo apt -y install nginx',
  before   => Exec['create /data/web_static/shared/']
}
exec { 'create /data/web_static/shared/':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
  before   => Exec['create /data/web_static/releases/test/']
}
exec { 'create /data/web_static/releases/test/':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  before   => Exec['add test content']
}
exec { 'add test content':
  provider => shell,
  command  => 'echo "Hello World!" > sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['create symbolic link to current']
}
exec { 'create symbolic link to current':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => File['/data/']
}
file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
  before  => Exec['serve current to hbnb_static']
}
exec { 'serve current to hbnb_static':
  provider => shell,
  command  => 'sudo sed -i "51i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default',
  before   => Exec['restart nginx']
}
exec { 'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart'
}

