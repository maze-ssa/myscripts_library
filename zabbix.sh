#!/bin/bash
echo "Enter your db_username===> "
read req1
db_user=$req1

echo "Enter your db_password===> "
read req2
db_password=$req2

echo "Enter your database name===> "
read req3
db_name=$req3
###############################################
echo "Install Zabbix Repo"
wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4+ubuntu22.04_all.deb
dpkg -i zabbix-release_6.0-4+ubuntu22.04_all.deb
apt update -y

###############################################
echo "Install Zabbix Server, Frontend Agent"
apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent

###############################################
echo "Install MYSQL-SERVER Package"
apt install mysql-server -y

##############################################
echo "Start MYSQL-SERVER service"
systemctl start mysql-server
systemctl enable mysql-server

###############################################
echo "Create inital database"
mysql -u root -p -e "create database zabbix character set utf8mb4 collate utf8mb4_bin; create user zabbix@localhost identified by '$db_password'; grant all privileges on zabbix.* to zabbix@localhost; set global log_bin_trust_function_creators = 1"

################################################
echo "On Zabbix server host import initial schema and data. You will be prompted to enter your newly created password."
zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p

################################################
echo "Disable log_bin_trust_function_creators option after importing database schema."
mysql -uroot -p -e "set global log_bin_trust_function_creators = 0"

################################################
echo "Configure Database for Zabbix Server"
sed -i 's/DBUser=/DBUser=$db_user/g' /etc/zabbix/zabbix_server.conf
sed -i 's/DBName=/DBName=$db_name/g' /etc/zabbix/zabbix_server.conf
sed -i 's/DBPassword=/DBPassword=$db_password/g' /etc/zabbix/zabbix_server.conf

###################################################
echo "Start Zabbix server and agent processes"
systemctl restart zabbix-server zabbix-agent apache2
systemctl enable zabbix-server zabbix-agent apache2