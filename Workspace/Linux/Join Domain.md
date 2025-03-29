# Linux

## Join Domain

### Install Required Packages (realmd, sssd, ...)

yum install -y realmd oddjob oddjob-mkhomedir sssd adcli

### Discover Domain

realm discover <domain_name>

### Join Domain

realm join --user=<username> <domain_name>
