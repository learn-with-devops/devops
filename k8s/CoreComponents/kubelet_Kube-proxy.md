## Kubelet



    - An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.

    - The kubelet takes a set of PodSpecs that are provided through various mechanisms and ensures that 
      the containers described in those PodSpecs are running and healthy. 
      The kubelet doesn’t manage containers which were not created by Kubernetes.
      
      
 ## Kube-Proxy
 
 

    - kube-proxy is a network proxy that runs on each node in the cluster.

    - It enables the Kubernetes service abstraction by maintaining network rules on the host and performing connection forwarding.

    - kube-proxy is responsible for request forwarding. kube-proxy allows TCP and UDP stream forwarding or round robin TCP and UDP forwarding across a set of backend functions. 
