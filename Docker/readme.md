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
