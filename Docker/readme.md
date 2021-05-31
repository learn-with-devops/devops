
## Create a Docker Container with Below requirements:
    - Copy a test.sh file into Docker | it will generate hello.txt file
    - Get a copy of generated hello.txt file into LocalHost machine with perticular user ( anand user) permission.
    - All this done while converting an Image to Container.
    
  Ans: 
    docker run -it -v /root/dk/:/opt --name <container Name> b8a416efc2c8 bash -c "sh /opt/test.sh && chown 1001 test.html"

## Multi Staged docker container
    
    # syntax=docker/dockerfile:1
    FROM golang:1.16 AS builder
    WORKDIR /go/src/github.com/alexellis/href-counter/
    RUN go get -d -v golang.org/x/net/html  
    COPY app.go    .
    RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

    FROM alpine:latest  
    RUN apk --no-cache add ca-certificates
    WORKDIR /root/
    COPY --from=builder /go/src/github.com/alexellis/href-counter/app .
    CMD ["./app"]  

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
            
---------------------------------------------------------------
                        
## COPY and ADD differences
            
Difference-1 👎           

If you want to add a xx.tar.gz to a /usr/local in container, unzip it, and then remove the useless compressed package.

For COPY:

        COPY resources/jdk-7u79-linux-x64.tar.gz /tmp/
        RUN tar -zxvf /tmp/jdk-7u79-linux-x64.tar.gz -C /usr/local
        RUN rm /tmp/jdk-7u79-linux-x64.tar.gz

For ADD:

        ADD resources/jdk-7u79-linux-x64.tar.gz /usr/local/

ADD supports local-only tar extraction. Besides it, COPY will use three layers, but ADD only uses one layer.

            
            
Difference-2 👎

- COPY copies a file/directory from your host to your image.

- ADD copies a file/directory from your host to your image, but can also fetch remote URLs, extract TAR files, etc... 

--------------------------------------------------------------------------------------

ENTRYPOINT Vs CMD
            
    I'll add my answer as an example1 that might help you better understand the difference.

    Let's suppose we want to create an image that will always run a sleep command when it starts. We'll create our own image and specify a new command:

            FROM ubuntu
            CMD sleep 10

    Building the image:

            docker build -t custom_sleep .
            docker run custom_sleep
            # sleeps for 10 seconds and exits

    What if we want to change the number of seconds? We would have to change the Dockerfile since the value is hardcoded there, or override the command by providing a different one:

            docker run custom_sleep sleep 20

    While this works, it's not a good solution, as we have a redundant "sleep" command. Why redundant? Because the container's only purpose is to sleep, so having to specify the sleep command explicitly is a bit awkward.

    Now let's try using the ENTRYPOINT instruction:

            FROM ubuntu
            ENTRYPOINT sleep

    This instruction specifies the program that will be run when the container starts.

    Now we can run:

            docker run custom_sleep 20

    What about a default value? Well, you guessed it right:

            FROM ubuntu
            ENTRYPOINT ["sleep"]
            CMD ["10"]

    The ENTRYPOINT is the program that will be run, and the value passed to the container will be appended to it.

    The ENTRYPOINT can be overridden by specifying an --entrypoint flag, followed by the new entry point you want to use.

------------------------------------------------------------------------------------------------------

### From inside of a Docker container, how do I connect to the localhost of the machine?

    Use --network="host" in your docker run command, then 127.0.0.1 in your docker container will point to your docker host.

--------------------------------------------------------------------------------------------------------
### How to copy Docker images from one host to another without using a repository

Ref  : https://medium.com/@BeNitinAgarwal/understanding-the-docker-internals-7ccb052ce9fe

You will need to save the Docker image as a tar file:

    docker save -o <path for generated tar file> <image name>

Then copy your image to a new system with regular file transfer tools such as cp, scp or rsync(preferred for big files). After that you will have to load the image into Docker:

    docker load -i <path to image tar file>

PS: You may need to sudo all commands.

EDIT: You should add filename (not just directory) with -o, for example:

docker save -o c:/myfile.tar centos:16


    Commands 👎
        Transferring a Docker image via SSH, bzipping the content on the fly:

        docker save <image> | bzip2 | \
             ssh user@host 'bunzip2 | docker load'

        It's also a good idea to put pv in the middle of the pipe to see how the transfer is going:

        docker save <image> | bzip2 | pv | \
             ssh user@host 'bunzip2 | docker load'

-------------------------------------------------------------------------------------
            
### Understanding the Docker Internals        
            
   ![image](https://user-images.githubusercontent.com/51190838/118591709-455a0d00-b7c2-11eb-8d44-ad168bb52f1b.png)
            
Docker takes advantage of several features of the Linux kernel to deliver its functionality.
            
Namespaces 👎
        Docker makes use of kernel namespaces to provide the isolated workspace called the container. When you run a container, Docker creates a set of namespaces for that container. These namespaces provide a layer of isolation. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.

                    Docker Engine uses the following namespaces on Linux:

            PID namespace for process isolation.
            NET namespace for managing network interfaces.
            IPC namespace for managing access to IPC resources.
            MNT namespace for managing filesystem mount points.
            UTS namespace for isolating kernel and version identifiers.
            
Cgroups 👎

        Docker also makes use of kernel control groups for resource allocation and isolation. A cgroup limits an application to a specific set of resources. Control groups allow Docker Engine to share available hardware resources to containers and optionally enforce limits and constraints.

        Docker Engine uses the following cgroups:

            Memory cgroup for managing accounting, limits and notifications.
            HugeTBL cgroup for accounting usage of huge pages by process group.
            CPU group for managing user / system CPU time and usage.
            CPUSet cgroup for binding a group to specific CPU. Useful for real time applications and NUMA systems with localized memory per CPU.
            BlkIO cgroup for measuring & limiting amount of blckIO by group.
            net_cls and net_prio cgroup for tagging the traffic control.
            Devices cgroup for reading / writing access devices.
            Freezer cgroup for freezing a group. Useful for cluster batch scheduling, process migration and debugging without affecting prtrace.

Union File Systems 👎

    Union file systems operate by creating layers, making them very lightweight and fast. Docker Engine uses UnionFS to provide the building blocks for containers. Docker Engine can use multiple UnionFS variants, including AUFS, btrfs, vfs, and devicemapper.

Container Format 👎

    Docker Engine combines the namespaces, control groups and UnionFS into a wrapper called a container format. The default container format is libcontainer.

Security 👎

    Docker Engine makes use of AppArmor, Seccomp, Capabilities kernel features for security purposes.

        AppArmor :  allows to restrict programs capabilities with per-program profiles.
        Seccomp : used for filtering syscalls issued by a program.
        Capabilties : for performing permission checks.
