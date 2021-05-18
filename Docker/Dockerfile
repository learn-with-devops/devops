FROM python:3.6.8

RUN groupadd -r app && useradd -r -g app app

WORKDIR /se_pv

COPY requirements.txt /se_pv/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -m venv /se_pv/env

RUN echo "source activate /se_pv/env" >> ~/.bashrc
COPY . /se_pv

RUN python setup.py develop
RUN chmod +x /se_pv/main_pipeline_script.py
RUN chown -R app:app /se_pv

EXPOSE 22
USER app
ENTRYPOINT [ "python3", "/se_pv/main_pipeline_script.py"]
-------------------------------------------------------------------------------------------

FROM centos:latest

MAINTAINER Anand Reddy < anand@gmail.com >

ENV workdir
RUN yum -y update && yum -y install httpd && rm -rf /var/www/html/* 

WORKDIR /var/www/html

COPY index.html /var/www/html

EXPOSE 80

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]


-------------------------------------------------------------------------------------------------------------------------------

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

--------------------------------------------------------------------------------------------------------------------------


# Downlodng the CentOS BAse Image
FROM  centos:latest

MAINTAINER Anand Reddy <anand@gmail.com>

LABEL Vendor="CentOS" \
      License=GPLv2 \
      Version=2.4.6-40

# Upadating the Packages
RUN yum -y update 

ENV wrd /var/www/html/

# Installing the Apache
RUN yum -y install httpd && rm -rf $wrd/*

WORKDIR $wrd

COPY index.html $wrd

#ADD http://apachemirror.wuchna.com/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz /opt

#RUN tar -xvf /opt/apache-maven-3.6.1-bin.tar.gz -C /opt/maven

VOLUME apache-backup $wrd

# ADD install_java.sh $pwd

# RUN chmod +x $pwd/install_java.sh

# CMD ["$pwd/install_java.sh"]

EXPOSE 80

ENTRYPOINT ["/usr/sbin/httpd","-D","FOREGROUND"]


