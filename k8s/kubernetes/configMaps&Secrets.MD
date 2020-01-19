
## Config Maps

If you want to make your containers are portable then use the ConfigMaps to do that.

                        or
                        
A ConfigMap stores configuration settings that your Kubernetes Pods consume.

Note:  
    
    These are desined to handle overall configuration of container and Sercrets are mainly designed to handle Sensitive data.

### Create a config Maps from defferent ways.

We can create a configMaps in 3 ways.

    - Directories
    - Files
    - Literal Values
    
Ref : https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/


## Secrets

To handle small amount of Sensitive data like passwords , tokens and keys etc..

Note:  
    - secrets are going to store inside ETCD database.
    - 1MB is the max size of each secret.
    - Values are going to stored in tmpfs folder.
    
    
## How to inject secrets to Pods ??

2 ways : 

  1. Volumes
  2. Env Variables
  
## Creating secrets in two ways??
  
  ![image](https://github.com/learn-with-devops/devops/blob/master/k8s/kubernetes/images/secrets_keys.PNG)
  
  
  1. Kubectl
  ![image](https://github.com/learn-with-devops/devops/blob/master/k8s/kubernetes/images/ks1.PNG)
  
  2. Manually
  ![image](https://github.com/learn-with-devops/devops/blob/master/k8s/kubernetes/images/ks2.PNG)
  ![image](https://github.com/learn-with-devops/devops/blob/master/k8s/kubernetes/images/ks3.PNG)
  



