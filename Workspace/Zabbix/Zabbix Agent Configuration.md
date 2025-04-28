# Zabbix

## Zabbix Agent Configuration (CentOS)

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
yum install -y zabbix-agent
```

### 3. Configure Zabbix Server

##### Zabbix Agent Config: /etc/zabbix/zabbix_agentd.conf

##### Zabbix Agent Log: /var/log/zabbix/zabbix_agentd.log

```bash
vi /etc/zabbix/zabbix_agentd.conf
```

```bash
Server=<zabbix-server-ip-or-dns>
ServerActive=<zabbix-server-ip-or-dns>
Hostname=<hostname-on-which-zabbix-agent-is-installed>
# Hostname must be exactly same as configured in Zabbix Server
```

### 4. Start and Enable Zabbix Agent

```bash
systemctl restart zabbix-agent
systemctl enable zabbix-agent
```

### 5. Post-Installation Configurations

#### 5.1. Open Zabbix Client Port in Firewall

```bash
firewall-cmd --permanent --zone=public --add-port=10050/tcp # Server to Agent
firewall-cmd --reload
```