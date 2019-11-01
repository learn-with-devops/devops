# Kubernetes

Reference : https://www.aquasec.com/wiki/display/containers/Kubernetes+Architecture+101

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
	
	
kubectl :  Command in line tool that interact with kube-apiserver and send commands to master node.Each command is converted into an API call.


								 
-------------------------------------------------------------------------

API-Server : Acts as a frient end for kubernetes.Users, management devices, CLI all talk to the api servers to intaract with kubernetes cluster.

etcd : It is going to store all clusters info and  multiple node and master  information

Shcedular : distributing work and containers acrross multiple nodes. It look for newly created containers and assign them to nodes.

Controllers :  These are the brain behind the container orchistration. They are notising and responding when nodes , containers went down. They take a decision to crete a new container when any container/node went down.

Container Runtime : Is an underlying s/w that is used to run containers. ex: docker

kubelet :  Is an agent that runs on each node.These are responsible for running the containers on nodes as expected.

Kubectl : Used to deploy and manage applications on kubernetes cluster. to get the cluster information, managing of other nodes.


----------------------------------------------------------

Deployments
pods
services
replica sets


------------------------------------------------


Problem With Normal-Container-Management :

 	- Scale-up/Scale-Down the containers.
 	- Load balancing of all containers.
 	- Self Healing of the containers & Servers.
 	- Scheduling 
 	- Networking
 	- Deployment
 	- Dashboard








------------------------------------------------

https://www.codeooze.com/windows-10/windows-10-ubuntu-vbox/









 
