#!/bin/bash
cd "$(dirname "$0")"

# must run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 
    exit 1
fi

# must be ubuntu 18.04
. /etc/lsb-release
if [ $DISTRIB_RELEASE != '18.04' ]; then
    echo "Ubuntu 18.04 required"
    exit 1
fi

# installing and setting up apache
apt install apache2 python3-pip php7.2 libapache2-mod-php7.2 certbot python-virtualenv python3-virtualenv certbot
a2enmod rewrite
a2enmod ssl
a2enmod php7.2

# setting up the virtual environment for python
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

# getting django going
python pyvhost/manage.py makemigrations
python pyvhost/manage.py makemigrations apache_config
python pyvhost/manage.py migrate
