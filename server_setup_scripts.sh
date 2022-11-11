#!/usr/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y install python3-pip
pip3 uninstall Fabric
sudo apt-get install -y libffi-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y build-essential
sudo apt-get install -y python3.4-dev
sudo apt-get install -y libpython3-dev
pip3 install pyparsing
pip3 install appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1
sudo apt install -y mysql-server
sudo apt-get install -y python3-dev
sudo apt-get install -y libmysqlclient-dev
sudo apt-get install -y zlib1g-dev
sudo pip3 install -y mysqlclient
sudo pip3 install SQLAlchemy
sudo pip3 install Flask
sudo pip3 install flask-cors
sudo apt-get install -y curl
sudo apt-get install -y wget
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install semistandard --global
sudo apt-get install -y vim
sudo apt-get install -y nginx
sudo apt-get install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
