## Networking Concepts

### PING


1. Ping Port Number ??

        Port numbers are layer-4 addresses for some layer-4 protocols, e.g. TCP or UDP. Other layer-4 protocols may use something else, or nothing at all.

        ICMP does not use port numbers. ICMP acts like a layer-4 protocol, but it is really an integral part of IP, a layer-3 protocol that knows nothing about port numbers. 
        See RFC 792, INTERNET CONTROL MESSAGE PROTOCOL:

          ICMP, uses the basic support of IP as if it were a higher level protocol, however, ICMP is actually an integral part of IP, and must be implemented by every IP module.

        Ping, itself, is an application that uses ICMP echo requests and replies.
        
        Ref : https://networkengineering.stackexchange.com/questions/42463/ping-port-number
