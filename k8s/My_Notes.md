# Kubernetes

#### Deploying an Helloworld Application.
    
    kubectl run helloworld --image=karthequian/helloworld --port=80
    
#### List out the deployments

    kubectl get deployments
    
#### List out the Pods

    kubectl get pods
    
#### Describe the pods

    kubectl describe pod helloworld-57d8dcf55f-jj7mn
    
#### Describe the Deployments

    kubectl describe deployment helloworld
    
#### List out the replicaSets

    kubectl get rs

#### List Out the Services

    kubectl get services
    
#### 
