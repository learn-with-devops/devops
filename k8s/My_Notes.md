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
    
#### Expose the Deployment to the Outer World
 
    kubectl expose deployment helloworld --type=NodePort
    
#### Then Type below to see the port

    kubectl get services  # Use that Port for accessing from Internet
    
#### If you want to see the deployment service in YAML format.

    kubectl get deploy/helloworld -o yaml
    
#### Scale Up the Containers count

    kubectl scale --replicas=10 deploy/helloworld
    
   
