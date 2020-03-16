## K8s Certification Exam Preparation-Monitoring/Logging

### k8s-Monitoring : 

  How to monitoring a resource consumption in k8s cluster ??
  
    - As of now we don't have k8s built-in monitoring solution to monitor the nodes , pods , cpu and memory consumption etc..
      However , N-number of open source solutions avilable for monitoring the above..
      
      Ex: 1. Metrics-Server 
          2. Promitheus
          3. Elastic Stack
          4. DataDog
          5. Dynatrace

#### Metrics-Server

      HeapSter is the original one...Now it is depricated and slimdown like metrics-Server.
      
        - One metrics server enough for one kubernetes cluster.
        - It is an In-Memory monitoring solution and it does not store any thing on disk.So ,we cannot see the historical data with this monitoring solution..So , we can go with other monitoring solutions.

    Note: 
    
      CADVISER is responsible on the node to expose the metrics to the monitoring solution with the help of KUBELET.
    
    Command: 
    
        - Find a Highest CPU/RAM consumed nodes.

            kubectl top nodes

        - Find a Highest CPU/RAM consumed Pods.

            kubectl top pods
      
      

