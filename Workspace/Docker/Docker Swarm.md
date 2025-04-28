# Docker

## Docker Swarm Initialization

### 1. Install & Enable Docker Service

[Install Docker Engine on RHEL](https://docs.docker.com/engine/install/rhel/)

### 2. Swarm Mode Routing Mesh (Overlay Network - Ingress)

[Use Swarm mode routing mesh](https://docs.docker.com/engine/swarm/ingress/)
<iframe width="560" height="315" src="https://www.youtube.com/embed/gJVcKVdYhpI?si=rUhbdhjW1VutjHf3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### 3. Open Firewall Ports

To use the ingress network in the swarm, the following ports must be opened between <u>**all the swarm nodes</u> before Swarm mode is enabled**:

- Port **2377 TCP** for communication with and between manager nodes
- Port **7946 TCP/UDP** for container network discovery.
- Port **4789 UDP** (configurable) for the container ingress network.

The **published port** must also be opened <u>between the swarm nodes and any external resources, such as an external load balancer</u>, that require access to the port.
<br>
##### On Manager Nodes

```bash
firewall-cmd --permanent --zone=public --add-port=2377/tcp
firewall-cmd --permanent --zone=public --add-port=7946/tcp
firewall-cmd --permanent --zone=public --add-port=4789/udp
firewall-cmd --reload
```

##### On Worker Nodes

```bash
firewall-cmd --permanent --zone=public --add-port=7946/tcp
firewall-cmd --permanent --zone=public --add-port=4789/udp
firewall-cmd --reload
```

### 4. Initialize Docker Swarm in Manager Leader Node

```bash
docker swarm init
```

##### Verify Docker Swarm on Manager Leader Node

```bash
docker node ls
```

##### After Docker Swarm is initialized, (2) new Networks will be created:

```bash
docker network ls

NETWORK ID     NAME              DRIVER    SCOPE
2ad296c78140   bridge            bridge    local
c203c6067d76   docker_gwbridge   bridge    local    <==
5e1942720b8b   host              host      local
p9a6s9jh9w1k   ingress           overlay   swarm    <==
245df52fc678   none              null      local
```

### 5. Join Docker Swarm as Manager Node

##### On Existing Manager Node

```bash
docker swarm join-token manager
```

Copy **docker swarm join** command and execute in New Manager node.

```bash
docker swarm join --token <token> <manager-node-ip-or-dns>:2377
```

### 6. Join Docker Swarm as Worker Node

```bash
docker swarm join-token worker
```

Copy **docker swarm join** command and execute in New Worker node.

```bash
docker swarm join --token <token> <manager-node-ip-or-dns>:2377
```

### 7. Install Docker Swarm Visualizer

```bash
docker service create \
  --name=swarm-visualizer \
  --publish=8888:8080/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  dockersamples/visualizer
```

### 8. Create Service is Docker Swarm

```bash
docker service create \
    --name <service-name>
    --publish published=<PUBLISHED_PORT>,target=<CONTAINER_PORT> \
    --constraint=node.role==worker \
    --replicas <number-of-replicas> \
    <image-name>
```

- The <PUBLISHED_PORT> is the port where the swarm makes the service available.
- If it is omitted, a random high-numbered port is bound.
- The <CONTAINER_PORT> is the port where the container listens.
- This parameter is required.
<br>
- On the swarm nodes themselves, the published port may not actually be bound, but the routing mesh knows how to route the traffic and prevents any port conflicts from happening.
- The routing mesh listens on the published port for any IP address assigned to the node.
- For externally routable IP addresses, the port is available from outside the host.
- For all other IP addresses the access is only available from within the host.

### 9. Bypass Routing Mesh

- By default, swarm services which publish ports do so using the routing mesh.
- The routing mesh can be bypassed, so that when the bound port is accessed on a given node, the instance of the service running on that node is always being accessed.
- This is referred to as **host mode**.
- To bypass the routing mesh, use the **long --publish** service and set **mode=host**.

```bash
docker service create \
    --name <service-name>
    --publish published=<PUBLISHED_PORT>,target=<CONTAINER_PORT>,mode=host \    <==
    --replicas <number-of-replicas> \
    <image-name>
```

### 10. Rebalance Containers

Scneario:
1. A service creates (2) containers on Worker-1 and (2) containers on Worker-2
2. Worker-2 fails and Swarm reschedules its containers to healthy nodes which, in this case, Worker-1
3. Later, Worker-2 comes back online, but Swarm does not automatically move its containers back to the original node, Worker-2, and all (4) containers are running on Worker-01

##### Manual Rebalance

**1. Remove and Recreate the Service**

```bash
docker service update --force <service_name>
```

**2. Scale Down and Scale Back Up**

```bash
docker service scale <service_name>=<replicas>
```