FROM centos:latest

MAINTAINER Anand Reddy < anand@gmail.com >

ENV workdir
RUN yum -y update && yum -y install httpd && rm -rf /var/www/html/* 

WORKDIR /var/www/html

COPY index.html /var/www/html

EXPOSE 80

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]




FROM centos:latest

MAINTAINER Anand Reddy < anand@gmail.com >

ENV workdir /var/www/html

RUN yum -y update && yum -y install httpd && rm -rf $workdir/* 

WORKDIR $workdir

COPY index.html $workdir

ADD python.py $workdir

VOLUME /app

EXPOSE 80

CMD python python.py

ADD http://mirrors.estointernet.in/apache/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz -C /tmp

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]
