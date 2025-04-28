#! /bin/bash

export DEBIAN_FRONTEND=noninteractive
apt-get update 
apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade
apt-get install -y ruby ruby-dev
yes | gem install jekyll
