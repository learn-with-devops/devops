    1  clear
    2  yum install java-1.8* wget -y
    3  alternatives --config java
    4  clear
    5  cd /opt/
    6  wget https://sonatype-download.global.ssl.fastly.net/repository/repositoryManager/3/nexus-3.16.2-01-unix.tar.gz
    7  clear
    8  ls
    9  tar -xvf nexus-3.16.2-01-unix.tar.gz
   10  ls
   11  rm -rf nexus-3.16.2-01-unix.tar.gz
   12  clear
   13  ls
   14  cd nexus-3.16.2-01/
   15  ls
   16  cd bin/
   17  ls
   18  ./nexus status
   19  useradd nexus
   20  cd ..
   21  cd .
   22  cd ..
   23  ls -ltr
   24  chown -R nexus:nexus nexus-3.16.2-01/ sonatype-work/
   25  ls -ltr
   26  cd nexus-3.16.2-01/
   27  ls
   28  cd bin/
   29  ls
   30  vi nexus.rc
   31  pwd
   32  ln -s /opt/nexus-3.16.2-01/bin/nexus /etc/init.d/nexus
   33  cd
   34  nexus status
   35  service nexus status
   36  cd /etc/init.d
   37  sudo chkconfig --add nexus
   38  sudo chkconfig --levels 345 nexus on
   39  service nexus start
   40  service nexus stop
   41  cd
   42  su - nexus
   43  service nexus restart
   44  exit
   45  history
