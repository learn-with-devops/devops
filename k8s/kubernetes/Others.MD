## Scheduling

### Manual Scheduling

    we can schedule manually by specifing the "nopeName" in manifest file...
    There is no way to use kubectl to update the pod once its created.But, you can use with the API to pass.
    
    ex: 
       spec:
        nodeName: server02

### Diplay all the Objects(pods , rs , rc, deployment etc) with env as prod.

    kubectl get all --selector env=prod

### Filter a pod with multiple lables

    kubectl get all --selector env=prod,bu=finance,tier=frontend
    
## Taints & Tolerations

    are used to set restrictions on what pods schedule on a node.
    
    Note: 
    
        Taints are set to Nodes.
        Tolerations are set to Pods.
        
        - Taints --> Nodes
            kubectl taints nodes node-name key=value:taint-effect     // taint-effects : 3 types   NoSchedule|PreferNoSchedule|NoExecute
            
            ex : 
                kubectl taints nodes server-01 app=blue:NoSchedule
                
           
