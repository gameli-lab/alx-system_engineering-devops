# Setting up an ubuntu sever

exec { 'install':
provider => shell,
command  => 'apt-get -y update; apt-get -y nginx; echo "Hello World!" > index.html, cp index.html /var/www/html/index.html, sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/jw.org permanent;/" /etc/nginx/sites-available/default; service nginx start',
}
