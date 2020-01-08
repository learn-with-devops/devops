# Architecture types 
	- Monolithic ( thease are loosly coupled and if any function down entire application down .. ex: WAR/JAR )
	- MicroService ( Loosly coupled and each service work independently. So , If any function down also it will work with other microservices )

# Container Orchistration Engine Advantages

	- Clustering
	- Scheduling
	- Scalabilities
	- Load Balancing
	- Fault Tolerence
	- Deployment
	
# Kubernetes

Reference : https://www.aquasec.com/wiki/display/containers/Kubernetes+Architecture+101

	Kubernetes is an open source orchestration tool developed by Google for managing microservices or containerized applications across a distributed cluster of nodes. 
	Kubernetes provides highly resilient infrastructure with zero downtime deployment capabilities, automatic rollback, scaling, and self-healing of containers (which consists of auto-placement, auto-restart, auto-replication , and scaling of containers on the basis of CPU usage).

Kubernetes Components:
-----------------------

Master :
--------

	- etcd-cluster(Storage )  : It is Simple, Distributed key-value storage which is used to store the 
											- kubernetes cluster data ( such as Number of pods , their state and namespace ), 
											- API objects
											- service_discovery details.
	
	- kube-apiserver          :  Kubernetes API server is the central management entity that receives 
											- all REST requests for modifications (to pods, services, replication sets/controllers and others), 
											- serving as frontend to the cluster.
											
	- Cloud Control Manager   : Is responsible for all nodes need to be up. When node terminated it will make it up again.
	
	- Kube Control Manager    :  runs a number of distinct controller processes in the background (for example, replication controller controls 
	                             number of replicas in a pod, endpoints controller populates endpoint objects like services and pods, and others) to regulate the shared state of the cluster and perform routine tasks.
								 
	- Kube-Schedular          : helps schedule the pods (a co-located group of containers inside which our application processes are running) on the various nodes based on resource utilization.
	
Slave: 
-------

	- kube-proxy: a proxy service that runs on each worker node to deal with individual host subnetting and expose services to the external world. It performs request forwarding to the correct pods/containers across the various isolated networks in a cluster.
	
	- kubelet:  the main service on a node, regularly taking in new or modified pod specifications (primarily through the kube-apiserver) and ensuring that pods and their containers are healthy and running in the desired state. This component also reports to the master on the health of the host where it is running.
	
	- POD
	
	- Container
	
CLI for Interatcting to Master :
--------------------------------

	- kubectl :  Command in line tool that interact with kube-apiserver and send commands to master node.Each command is converted into an API call.



Notes: 
------

 	- Kubernetes supports 5000 worker nodes to attach to master.
	
	- pods : Ex..I VMWare terminology a POD is a VM..and A POD can contain one or more containers. With the help of POD we can deploy multiple dependent containers together as a single unit. 
	
	
Other Terminologies:
--------------------

	- Fault Tollerence ( Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of (or one or more faults within) some of its components. )
	


Kubernetes Installation ways:
-----------------------------

1. Play-with-k8s 

		- kubeadm init

		kubeadm join 172.18.0.34:6443 --token vlgle2.swtx5i0tpppuzz3b \
		    --discovery-token-ca-cert-hash sha256:c95829447a486516b6302a564e83f55178935ddf4172e89f111c17decced82a0


		- kubectl apply -n kube-system -f  "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 |tr -d '\n')"

2. Minikube

3. Kubeadm


