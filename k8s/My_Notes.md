# Kubernetes

### Chat-Sheet : https://kubernetes.io/docs/reference/kubectl/cheatsheet/

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
    
#### Deploy a Service on Specific Node by using below procedure

     You can try this code:

        kubectl label node [name_of_node] node-short-name=node-1 
        
     Create yaml file (first.yaml)

        apiVersion: v1
        kind: Pod
        metadata:
         name: nginxtest 
         labels:
          env: test
        spec:
         containers:
         - name: nginx 
           image: nginx 
           imagePullPolicy: IfNotPresent
         nodeSelector: 
          node-short-name: node-1
         
     Create a pod

        kubectl create –f  first.yaml

    Reference Link :  https://stackoverflow.com/questions/27832984/will-can-kubernetes-run-docker-containers-on-the-master-nodes
    
#### Scale Up the Containers count

    kubectl scale --replicas=10 deploy/helloworld
    
#### List out the pod running nodes with all details

    kubectl get pod -o=custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName --all-namespaces
    or
    kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name --all-namespaces
    or 
    kubectl get pod --all-namespaces -o json | jq '.items[] | .spec.nodeName + " " + .status.podIP'
    
#### 
