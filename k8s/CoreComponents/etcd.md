## Etcd


  Etcd is a crucial component for Kubernetes as it stores the entire state of the cluster: 
            its configuration, specifications, and the statuses of the running workloads.


  Etcd’s watch functionality is used by Kubernetes to monitor changes to either the actual or the desired state of its system. 
  If they are different, Kubernetes makes changes to reconcile the two states. Every read by the kubectl command is retrieved 
  from data stored in Etcd, any change made (kubectl apply) will create or update entries in Etcd, and every crash will trigger value changes in etcd.



## Installation :

  wget https://github.com/etcd-io/etcd/releases/download/v3.3.25/etcd-v3.3.25-linux-amd64.tar.gz
  tar -xvf etcd-v3.3.25-linux-amd64.tar.gz
  cd etcd-v3.3.25-linux-amd64
  
  Run in Background: ./etcd &
  
  Insert some Data :
  
      ./etcdctl set Name Anand
      
  Get Data: 
      
      ./etcdctl get Name
