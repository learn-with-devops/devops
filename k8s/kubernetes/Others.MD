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
        
        
        Note :  It has a limitations .... i.e we cannot say that deploy on any Large/Medium nodes and we cannot say don't deploy on small node. ( We can achive this with Node_Afinity )
        
        
        #### Example

            spec:
                  affinity:
                      nodeAffinity:
                        preferredDuringSchedulingIgnoredDuringExecution:
                          nodeSelectorTerms:
                            - matchExpressions:
                              - key: size
                                operator: Exists/IN
                                values: 
                                    - Large
                                    - Medium

#### Node Affinity Example

                    apiVersion: apps/v1
                    kind: Deployment
                    metadata:
                      name: blue
                    spec:
                      replicas: 6
                      selector:
                        matchLabels:
                          run: nginx
                      template:
                        metadata:
                          labels:
                            run: nginx
                        spec:
                          containers:
                          - image: nginx
                            imagePullPolicy: Always
                            name: nginx
                          affinity:
                            nodeAffinity:
                              requiredDuringSchedulingIgnoredDuringExecution:
                                nodeSelectorTerms:
                                - matchExpressions:
                                  - key: color
                                    operator: In
                                    values:
                                    - blue

## Resource Limit

    We can limit the resources by specifing the things like below.
    
            spec: 

                resources:
                  requests:
                    memory: "64Mi"
                    cpu: "250m"
                  limits:
                    memory: "128Mi"
                    cpu: "500m"
                    
                    
 ## DaemomnSet
 
 
