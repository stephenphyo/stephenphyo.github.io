# Linux

## MySQL 8.0 Installation on CentOS 9

### Download and Prepare MySQL Repository

```bash
wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
rpm -Uvh mysql80-community-release-el7-3.noarch.rpm
rm -rf mysql80-community-release-el7-3.noarch.rpm
```

### Install MySQL Server

```bash
yum install -y mysql-server
```

### Start and Enable MySQL Service

```bash
systemctl restart mysqld
systemctl enable mysqld
```

### Post-Installation Configuration

```bash
mysql_secure_installation
```

#### Temporary Root Password

When installing MySQL on CentOS 9, a temporary root password is generated.
Sometimes, the root password is empty.

##### View Temporary Root Password

```bash
grep 'password' /var/log/mysql/mysqld.log
```

### Enable MySQL Ports in Firewall

```bash
firewall-cmd --permanent --zone=public --add-port=3306/tcp
firewall-cmd --reload
```