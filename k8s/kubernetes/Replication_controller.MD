## Replication controller

Ensure that a specified number of pods runs at a time.( High avilab ility & Load Balancing of POD's )
  - If pods are less than specified then it will create required.
  - If the pods are more than specified then it will decrese the pods count.

 #### Note :  
    
      Replication controller manage the pods count based on **Labels**
 
      - Replication Controller   ----- OLD
      - RelicaSet                ----- New
 
------------------

## Replication Controller commands

- Create a Replication Controller
    
      kubectl create -f nginx-rc.yml
  
- ListOut the Replication Controllers
  
      kubectl get rc
  
- Describe RC
  
      kubectl describe rc nginx-rc
  
- ListOut the pods thet belong to the single RC
  
      kubectl get pods -l app=nginx-app
  
- Update/ScaleUp/ScaleDown the Pods
  
      kubectl scale rc nginx-rc --replicas=5
  
--------------------------------------

## Replica-Set:

Replica-Set is next generation to the replication-controllers.

ReplcaSet. ----> supports----> Set-Based-Selectors
Replication-Controllers  ----> supports ---> Eqality-based-selectors.

