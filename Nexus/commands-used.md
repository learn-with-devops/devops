clear
yum install java-1.8* wget -y
alternatives --config java
clear
cd /opt/
wget https://sonatype-download.global.ssl.fastly.net/repository/repositoryManager/3/nexus-3.16.2-01-unix.tar.gz
clear
ls
tar -xvf nexus-3.16.2-01-unix.tar.gz
ls
rm -rf nexus-3.16.2-01-unix.tar.gz
clear
ls
cd nexus-3.16.2-01/
ls
cd bin/
ls
./nexus status
useradd nexus
cd ..
cd .
cd ..
ls -ltr
chown -R nexus:nexus nexus-3.16.2-01/ sonatype-work/
ls -ltr
cd nexus-3.16.2-01/
ls
cd bin/
ls
vi nexus.rc
pwd
ln -s /opt/nexus-3.16.2-01/bin/nexus /etc/init.d/nexus
cd
nexus status
service nexus status
cd /etc/init.d
sudo chkconfig --add nexus
sudo chkconfig --levels 345 nexus on
service nexus start
service nexus stop
cd
su - nexus
service nexus restart
exit
history
