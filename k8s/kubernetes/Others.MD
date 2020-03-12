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
    
## Taints & Tolerations ( How to restrict what pods are placed on what nodes )

    are used to set restrictions on what pods schedule on a node.
    
    Remeber : we cannot able to restrict a pod to run on specific node.
    
    Note: 
    
        1. Taints are set to Nodes.
        2. Tolerations are set to Pods.
        
        - Taints --> Nodes
            kubectl taints nodes node-name key=value:taint-effect     // taint-effects : 3 types   NoSchedule|PreferNoSchedule|NoExecute
            
            ex : 
                kubectl taints nodes server-01 app=blue:NoSchedule
                
        - Tolerations --> POds
        
            ex: 
                    spec:
                        tolerations:
                            - key: "app"
                              operator: "equal"
                              value: "blue"
                              effect: "NoSchedule"
                
           
         Question : Create a taint on node01 with key of 'spray', value of 'mortein' and effect of 'NoSchedule'
         
         Ans: kubectl taint node node01 spray=mortein:NoSchedule

  #### Example for Tolarent and Taints
  
            Ex: apiVersion: v1
                kind: Pod
                metadata:
                  name: bee
                spec:
                   containers:
                      - image: nginx
                        name: bee

                   tolerations:
                      - key: spray
                        value: mortein
                        effect: NoSchedule
                        operator: Equal
