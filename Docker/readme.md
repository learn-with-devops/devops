## Docker Union File System

    If I have a directory d1/, I know I can mount it at /mountPoint inside a Docker container by doing this:

    docker run -v /path/to/d1:/mountPoint ...
    However, I have two directories d1/ and d2/ (let's say they contain files a.txt and b.txt respectively).

    I want to mount the union of these two directories at /mountPoint in my container, i.e. I want /mountPoint/a.txt and /mountPoint/b.txt to exist.

    Given that Docker uses UnionFS a lot internally, I am rather hoping there are options to do a union mount at a specific path inside a container, but I can't find them if so.
    
Answer :

    One (probably obvious) workaround would be to install unionfs within the container and then unify all required partitions together with it:

    docker run -v /path/to/d1:/mnt/d1 -v /path/to/d2:/mnt/d2
    # and within docker container:
    mkdir -p /mnt/joined
    unionfs /mnt/d1=RO:/mnt/d2=RW /mnt/joined
    But it is ugly and I hope there is any better option.
    
    
Reference Link :

https://stackoverflow.com/questions/35891193/union-mounts-into-docker-containers


### Run a Docker Container on Specific Host ( Possible by using CONSTRAINTS option for services)

         version: "3"
        services:
          service1:
            image: localrepo/image1
            deploy:
              placement:
                constraints: [node.hostname == node1]
              replicas: 1
              resources:
                limits:
                  cpus: "1"
                  memory: 1000M
              restart_policy:
                condition: on-failure
            ports:
              - 8000:8000
            networks:
              - webnet

          service2:
            image: localrepo/image2
            deploy:
              placement:
                constraints: [node.hostname == node2]
              replicas: 1
              resources:
                limits:
                  cpus: "1"
                  memory: 500M
              restart_policy:
                condition: on-failure
            ports:
              - "8000:8000"
            networks:
              - webnet
        networks:
          webnet:


    Reference Link : https://stackoverflow.com/questions/39326602/docker-compose-swarm-force-containers-to-run-on-specific-hosts


Another Way :

            docker service create --name proxy --constraint "node.hostname!=node01" nginx

        Continuing the previous example, assuming your cluster with node-1 and node-2, you can run a MySQL server container on the cluster. When you run the container, you can use a constraint to ensure the database gets good I/O performance. You do this by filtering for nodes with flash drives:
        
        $ docker tcp://<manager_ip:manager_port>  run -d -P -e constraint:storage==ssd --name db mysql
f8b693db9cd6

$ docker tcp://<manager_ip:manager_port>  ps
CONTAINER ID        IMAGE               COMMAND             CREATED                  STATUS              PORTS                           NAMES
f8b693db9cd6        mysql:latest        "mysqld"            Less than a second ago   running             192.168.0.42:49178->3306/tcp    node-1/db

