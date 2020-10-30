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
    
Installation :

        Install OKey repository:
        # yum install http://repo.okay.com.mx/centos/7/x86_64/release/okay-release-1-1.noarch.rpm
        
        Install fuse-unionfs rpm package:
        # yum install fuse-unionfs
    
    
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


------------

## Docker Entrypoint vs CMD: Solving the Dilemma 

        In short, CMD defines default commands and/or parameters for a container. CMD is an instruction that is best to use if you need a default command which users can easily override. If a Dockerfile has multiple CMDs, it only applies the instructions from the last one.

        On the other hand, ENTRYPOINT is preferred when you want to define a container with a specific executable. You cannot override an ENTRYPOINT when starting a container unless you add the --entrypoint flag.

        Combine ENTRYPOINT with CMD if you need a container with a specified executable and a default parameter that can be modified easily. For example, when containerizing an application use ENTRYPOINT and CMD to set environment-specific variables.

## Shell and Exec Form

    Before we begin, it is important to discus the forms of instructions. Docker ENTRYPOINT and CMD can have two forms:

    - Shell form
    - Exec form

    The syntax for any command in shell form is:

        - Shell form
        <instruction> <command>
        The syntax for instructions in exec form is:

        - Exec form
        <instruction> [“executable”, “parameter”]
        You can write Docker CMD/ENTRYPOINT instructions in both forms:

        CMD echo “Hello World” (shell form)
        CMD ["echo", "Hello World"] (exec form)
        ENTRYPOINT echo "Hello World" (shell form)
        ENTRYPOINT ["echo", "Hello World"] (exec form)
        However, try to keep all your instructions in exec form to prevent potential performance issues.
        

## Exec form
        Exec form of ENTRYPOINT allows you to set commands and parameters and then use either form of CMD to set additional parameters that are more likely to be changed. ENTRYPOINT arguments are always used, while CMD ones can be overwritten by command line arguments provided when Docker container runs. For example, the following snippet in Dockerfile

            ENTRYPOINT ["/bin/echo", "Hello"]
            CMD ["world"]

            - when container runs as docker run -it <image> will produce output
               o/p : Hello world

            - but when container runs as docker run -it <image> John will result in
               o/p : Hello John

Ref : https://phoenixnap.com/kb/docker-cmd-vs-entrypoint#:~:text=CMD%20is%20an%20instruction%20that,container%20with%20a%20specific%20executable.
Ref : https://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/

---------------
### Print the Running container Names, ID and Statsu.

- Input: 
 
        CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS                    PORTS                    NAMES

        56489a32cb8c        83132b61eccf                  "bash"                   41 hours ago        Exited (0) 41 hours ago                            naughty_jang
        4b4933b40175        83119b65eccf                  "bash"                   41 hours ago        Exited (0) 41 hours ago                            suspicious_mcnulty
        3149e612f9f8        83119b6143cf                  "sh"                     43 hours ago        Exited (0) 41 hours ago                            thirsty_mestorf
        
 Command : 
 
        docker ps --format "{{.Names}}\t{{.ID}}\t{{.Status}}"
        
        output : 
        
            [root@ip-172-31-6-169 ~]# docker ps --format "{{.Names}}\t{{.ID}}\t{{.Status}}"

            apapche_app.4.s6i2u7xsetr3zx7yezn2azivg a715c247ba9f    Up 18 hours
            apapche_app.1.tjuie7d5mjjdgy36upxuv5h5u 3a88d2f401c0    Up 18 hours
