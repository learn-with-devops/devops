## NameSpaces

Kubernetes can offer multiple Kubernetes clusters on a single cluster, much like a virtual machine is an abstraction of its host. 

- According to the Kubernetes docs:

    Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called namespaces.


- The first three namespaces created in a cluster are always default, kube-system, and kube-public. While you can technically deploy within these namespaces, I recommend leaving these for system configuration and not for your projects. 

     - Default: is for deployments that are not given a namespace, which is a quick way to create a mess that will be hard to clean up if you do too many deployments without the proper information. I leave this alone because it serves that one purpose and has confused me on more than one occasion.
     
     - Kube-system is for all things relating to, you guessed it, the Kubernetes system. Any deployments to this namespace are playing a dangerous game and can accidentally cause irreparable damage to the system itself. Yes, I have done it; I do not recommend it.
    
     - Kube-public is readable by everyone, but the namespace is reserved for system usage.


### NameSpace commands

    - get a namespace
    
        kubectl get namespaces
        
    - list out the pods belong to a specific namespace.
    
        kubectl get pods --namespace=development/default
        
    - list out all the pods irrespective of namespaces
    
        kubectl get pods --all-namespaces
        
    - Set Development Namespace as Default namespace.
    
        kubectl config set-context $(kubectl config current-context) --namespace=development
        
        
