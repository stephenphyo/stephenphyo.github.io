# Load Balancing

## HAProxy & Keepalived

### Install HAProxy & Keepalived

```bash
yum install -y haproxy keepalived
```

### Create Health Check Script

```bash
touch /etc/keepalived/healthcheck.sh

cat >> /etc/keepalived/healthcheck.sh << 'EOF'
#!/bin/bash

errorExit() {
    echo "*** $@" 1>&2
    exit 1 
}

# Get parameters
IPADDRESS="$1"
PORT="$2"

# Default to localhost if IP address is not provided
if [ -z "$IPADDRESS" ]; then
  IPADDRESS="localhost"
fi

# Default to 6443 if port is not provided
if [ -z "$PORT" ]; then
  PORT="6443"
fi

curl --silent --max-time 2 --insecure https://localhost:$PORT/ -o /dev/null || errorExit "Error GET https://localhost:$PORT/"
if ip addr | grep -q "$IPADDRESS"; then
  curl --silent --max-time 2 --insecure https://$IPADDRESS:$PORT/ -o /dev/null || errorExit "Error GET https://$IPADDRESS:$PORT/"
fi
EOF
```

##### Change Permission

```bash
chmod +x /etc/keepalived/healthcheck.sh
```

### Configure Keepalived

```bash
mv keepalived.conf keepalived.conf.bk
touch keepalived.conf

cat >> /etc/keepalived/keepalived.conf <<EOF
vrrp_script check_health {
  script "/etc/keepalived/healthcheck.sh 192.168.1.210 6443"
  interval 3
  timeout 10
  fall 5
  rise 2
  weight -2
}

vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 1
    priority 100
    advert_int 5
    authentication {
        auth_type PASS
        auth_pass ALPHAbetagammatango@123
    }
    virtual_ipaddress {
        192.168.1.150
    }
    track_script {
        check_health
    }
}
EOF
```

### Allow HTTP in Firewall

```bash
firewall-cmd --add-rich-rule='rule protocol value="vrrp" accept' --permanent
firewall-cmd --reload
```

### Configure HAProxy

```bash
mv  /etc/haproxy/haproxy.cfg  /etc/haproxy/haproxy.cfg.bk
touch  /etc/haproxy/haproxy.cfg

cat >> /etc/haproxy/haproxy.cfg <<EOF

frontend k8s-frontend
  bind *:6443
  mode tcp
  option tcplog
  default_backend k8s-backend

backend k8s-backend
  option httpchk GET /healthz
  http-check expect status 200
  mode tcp
  option ssl-hello-chk
  balance roundrobin
    server kmaster1 192.168.1.191:6443 check fall 3 rise 2
    server kmaster2 192.168.1.192:6443 check fall 3 rise 2
    server kmaster3 192.168.1.193:6443 check fall 3 rise 2

EOF
```

### Set SELinux Boolean for HAProxy

```bash
setsebool -P haproxy_connect_any=1
```

### Start and Enable HAProxy

```bash
systemctl enable --now haproxy
```

### Start and Enable Keepalived

```bash
systemctl enable --now keepalived
```