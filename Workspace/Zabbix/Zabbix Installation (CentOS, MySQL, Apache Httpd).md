# Zabbix

## Zabbix Server Installation <br> (Zabbix 7.2, CentOS, MySQL, Apache Httpd)

### 1. Install Zabbix Repository

#### 1.1. Disable Zabbix Packages by EPEL

```bash
vi /etc/yum.repos.d/epel.repo
```

```bash
[epel]
...
excludepkgs=zabbix*
```

#### 1.2. Install Zabbix Repository

```bash
rpm -Uvh https://repo.zabbix.com/zabbix/7.2/release/centos/9/noarch/zabbix-release-latest-7.2.el9.noarch.rpm
dnf clean all
```

### 2. Install Zabbix Packages

```bash
yum install -y zabbix-server-mysql zabbix-web-mysql zabbix-apache-conf zabbix-sql-scripts zabbix-selinux-policy zabbix-agent
```

### 3. Create Initial Database

#### 3.1. Install MySQL Client

```bash
yum install -y mysql
```

#### 3.2. Create Zabbix Database and User

##### If MySQL is installed on Zabbix Server

```bash
mysql -uroot -p
```

```mysql
CREATE DATABASE zabbix character set utf8mb4 COLLATE utf8mb4_bin;
CREATE USER zabbix@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON zabbix.* TO zabbix@localhost;
SET GLOBAL log_bin_trust_function_creators = 1;
```

##### If MySQL is Remote Server (On Database Host)

```bash
mysql -uroot -p
```

```mysql
CREATE DATABASE zabbix character set utf8mb4 COLLATE utf8mb4_bin;
CREATE USER zabbix@localhost IDENTIFIED BY 'password';
CREATE USER zabbix@'%'' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON zabbix.* TO zabbix@localhost;
GRANT ALL PRIVILEGES ON zabbix.* TO zabbix@'%';
SET GLOBAL log_bin_trust_function_creators = 1;
```

#### 3.3 Import Initial Database Schema and Data

##### If MySQL is installed on Zabbix Server (On Zabbix Server Host)

```bash
zcat /usr/share/zabbix/sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p zabbix
```

##### If MySQL is Remote Server (On Zabbix Server Host)

```bash
zcat /usr/share/zabbix/sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -h <remote_mysql_svr> -uzabbix -p zabbix
```

#### 3.4. Disable 'log_bin_trust_function_creators' after Importing Database Schema

```mysql
SET GLOBAL log_bin_trust_function_creators = 0;
```

### 4. Configure Zabbix Server

#### 4.1. Zabbix Server Configuration

##### Zabbix Server Config: /etc/zabbix/zabbix_server.conf

##### Zabbix Web Config: /etc/zabbix/web/zabbix.conf.php

##### Zabbix Server Log: /var/log/zabbix/zabbix_server.log

```bash
vi /etc/zabbix/zabbix_server.conf
```

```bash
DBHost=<mysql-host-ip-or-dns>
DBName=zabbix # If default name is used
DBUser=zabbix # If default username is used
DBPassowrd=<password>
DBPort=3306 # If default port is used

ListenIP=<zabbix-server-ip-only>
ListenPort=10051
```

### 5. Post-Installation Configurations

#### 5.1. Open HTTP/HTTPS, Zabbix Ports in Firewall

```bash
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=public --add-service=https
firewall-cmd --permanent --zone=public --add-port=10050/tcp # Server to Agent
firewall-cmd --permanent --zone=public --add-port=10051/tcp # Agent to Server
firewall-cmd --reload
```

### 5.2. Set SELinux Boolean Value

```bash
setsebool -P zabbix_can_network on
```

- setsebool -P: This command sets SELinux boolean values with Persistent flag
- zabbix_can_network: This is the **SELinux boolean flag**, which controls whether Zabbix server is allowed to make network connections

### 6. Start and Enable Zabbix Server, Zabbix Agent and Other Services

```bash
systemctl restart zabbix-server zabbix-agent httpd php-fpm
systemctl enable zabbix-server zabbix-agent httpd php-fpm
```

### 7. Zabbix Frontend Configuration Setup

Go to: http://zabbix-server-ip-or-dns/zabbix

![xxxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/zabbix/zabbix-installation/zabbix-01.png)

<br>

![xxxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/zabbix/zabbix-installation/zabbix-02.png)

<br>

#### 7.1. Configure DB Connection

If the following error occurs, allow 'httpd' in SELinux.

![xxxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/zabbix/zabbix-installation/zabbix-07.png)

#### 7.1.1. Allow 'httpd' in SELinux

```bash
grep httpd_t /var/log/audit/audit.log | audit2allow -M httpd_custom
semodule -i httpd_custom.pp
```

- grep httpd_t /var/log/audit/audit.log: This searches the SELinux audit log for entries related to httpd_t context
- audit2allow -M httpd_custom: The filtered log entries from above are piped into audit2allow, which creates a custom SELinux module named httpd_custom to allow previously denied operations

- semodule -i: This installs the compiled policy package, making it active and applying the SELinux rule changes

#### 7.1.2. After 'httpd' is allowed in SELinux

![xxxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/zabbix/zabbix-installation/zabbix-03.png)

<br>

### 7.2. Configure Zabbix Server Settings

![xxxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/zabbix/zabbix-installation/zabbix-04.png)

### Finish Configuration Setup and Install

![xxxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/zabbix/zabbix-installation/zabbix-04.png)

<br>

![xxxl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/zabbix/zabbix-installation/zabbix-04.png)

<br>

### 8. Login to Zabbix Server

![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/zabbix/zabbix-installation/zabbix-08.png)

#### Default Username and Password

Username: **Admin** <br>
Passowrd: **zabbix**

### 9. Troubleshooting

#### Error: 'Cannot connect to the database' in Configure DB Connection

Root Cause: Httpd is blocked by SELinux

Resolution:

```bash
grep httpd_t /var/log/audit/audit.log | audit2allow -M httpd_custom
semodule -i httpd_custom.pp
```

#### Error: [Z3001] connection to database 'zabbix' failed: [2002] Can't connect to server on 'server-name' (13)

Root Cause: SELinux is Enforcing and 'zabbix_can_network' boolean flag is off

Resolution:

```bash
setsebool -P zabbix_can_network on
```

### Zabbix Ports

| Zabbix component    | Port number | Protocol | Type of connection |
| ------------------- | ----------- | -------- | ------------------ |
| Zabbix agent        | 10050       | TCP      | On Demand          |
| Zabbix agent 2      | 10050       | TCP      | On Demand          |
| Zabbix server       | 10051       | TCP      | On Demand          |
| Zabbix proxy        | 10051       | TCP      | On Demand          |
| Zabbix Java Gateway | 10052       | TCP      | On Demand          |
| Zabbix Web Service  | 10053       | TCP      | On Demand          |
| Zabbix Frontend     | 80          | HTTP     | On Demand          |
|                     | 443         | HTTPS    | On Demand          |
| Zabbix Trapper      | 10051       | TCP      | On Demand          |
