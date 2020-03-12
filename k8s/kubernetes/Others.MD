## Scheduling

#### Manual Scheduling

    we can schedule manually by specifing the "nopeName" in manifest file...
    There is no way to use kubectl to update the pod once its created.But, you can use with the API to pass.
    
    ex: 
       spec:
        nodeName: server02

#### Diplay all the Objects(pods , rs , rc, deployment etc) with env as prod.

    kubectl get all --selector env=prod

#### Filter a pod with multiple lables

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
         
         Que : Remove a taint on master node
         
         Ans: kubectl taint node master node-role.kubernetes.io/master:NoSchedule-   } - for removing the taint 

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
                        
    
   ## Node Selectors
   
        You can use node selectors to place specific pods on specific nodes, all pods in a project on specific nodes, or create a default node selector to schedule pods that do not have a defined node selector or project selector.
        
   #### Attach label to the node
   
        kubectl label nodes <node-name> <label-key>=<label-value>
        
        Ex: 
            kubectl label nodes node01 size=large
            
   #### Node Selector to create a Pod on specific place
   
        spec: 
            nodeSelector:
                size: Large
        
        
        
