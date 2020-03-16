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



    - Find a Highest CPU/RAM consumed nodes.

        kubectl top nodes

    - Find a Highest CPU/RAM consumed Pods.

        kubectl top pods
      
      

