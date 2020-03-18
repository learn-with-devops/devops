## Cluster Upgration.

### DRAIN :

    Used to move all the pods running on a present node to another and it will make the node as Un-Reachable for newly created pods.
    
    EX: kubectl drain node01
    
### CORDON :

    Used to make the node is Un-Reachable for new deployments and it will keep the pods on the same .
    
    Ex: kubectl cordon node02
    
### UN-CORDON

    Used to make the CORDON node to uvilable for the scheduler to schedule a New-Pods on it.
    
    Ex: kubectl uncordon node03
    
    
