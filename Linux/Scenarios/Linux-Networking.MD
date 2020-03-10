## Networking Concepts

### PING


1. Ping Port Number ??

        Port numbers are layer-4 addresses for some layer-4 protocols, e.g. TCP or UDP. Other layer-4 protocols may use something else, or nothing at all.

        ICMP does not use port numbers. ICMP acts like a layer-4 protocol, but it is really an integral part of IP, a layer-3 protocol that knows nothing about port numbers. 
        See RFC 792, INTERNET CONTROL MESSAGE PROTOCOL:

          ICMP, uses the basic support of IP as if it were a higher level protocol, however, ICMP is actually an integral part of IP, and must be implemented by every IP module.

        Ping, itself, is an application that uses ICMP echo requests and replies.
        
        Ref : https://networkengineering.stackexchange.com/questions/42463/ping-port-number


  2. Ping 8.8.8.8  // for google 
        
                ping priveteIP/PublicIP
                ping google.com
        
  3. Ping to the the server with DNS Name
  
                - first edit /etc/hosts file add like below

                        public/private-IP DNS-NAME-1 DNS-NAME2 ..

                        192.168.0.9 jenkins-server jenkins.in
                
   4. Ping 10 times to remote server
   
                ping -c 10 server-1
                
        
     Note : Some organizartions they will block a ICMP protocal ( PING protocal ) for their security resions.
            In that case you can use TELNET
            
            
## TELNET

        - Test the connection with the following way

                telnet server-1 22  // 22 is SSH port allowed by 2-nd server
                
                o/p :   Trying 172.31.35.191...
                        Connected to server-1.
                        Escape character is '^]'.
                        SSH-2.0-OpenSSH_7.4

        Note : the perticular PORT (80) got opened in remote server and when u tried to connect with telnet like "telnet jenkins.io 8080" your getting "connection refused eroor"
        
        i.e That mean , the perticular port running service not running properly.

## HOST FILE ( Old one replaced by DNS )

        You can use /etc/host for adding the DNS names for a server insted of DNS names..But , we cannot add n-number of servers into all the hosts.
        
        [root@ip-172-31-35-191 ~]# cat /etc/hosts
                127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
                ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

                172.31.45.83 jenkins-server  jenkins.io
        
        
## ROUTE

        used to check which router got attached to the server.
        
                route
                route -n
                
## NSLOOKUP / HOST

        Both are used to check the DNS/IP address connections/alias-names etc..
        
        nslookup www.google.com
        host www.google.com
        
        
         
