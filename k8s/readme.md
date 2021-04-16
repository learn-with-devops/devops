### Commands

- List out all the server resources
	 kubectl describe nodes | grep 'Name:\|  cpu\|  memory'
	 
## Volumes
	- PV , PVC ( Static )  and Storage Class ( Dynamic )
Notes: 
	- PV is created cluster level and pvc belong to namespace level
	- With Storage class you can automate the PV creation by specifing only pv claim.
	- If you declare PV then PVC you need to use the same labels, storage type, access modes and resources ( Some times if the avilable resources are more than u requested also fine ).

# Architecture types 
	- Monolithic ( thease are tightly coupled and if any function down entire application down .. ex: WAR/JAR )
	- MicroService ( Loosly coupled and each service work independently. So , If any function down then other functions of  microservices will run independently)

# Container Orchistration Engine Advantages

	- Clustering
	- Scheduling
	- Scalabilities
	- Load Balancing
	- Fault Tolerence
	- Deployment
	
# Pre-Requisites

	- security, certificates, networking and storage
	
# Architecture of Kubernetes
![image](https://github.com/learn-with-devops/devops/blob/master/k8s/kubernetes/images/k8s_architecture.jpg)
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
	
	- Controll Manager ( 4 types of controll managers)
		- Node Controller
		- Replication Controller
		- EndPoint Comtroller
		- Service account & Tocken Controller
		
	
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

3. Kubeadm with Google cloud

4. KOPS with AWS cloud

API Version
--------------------
![image](https://github.com/learn-with-devops/devops/blob/master/k8s/kubernetes/images/apiversion.PNG)

Note: 
	 -> Secrets ( v1 stable release) 
	 -> NameSpace ( v1 apiVersion)



OtherInformation 
--------------------

### DaemonSet :

	- How do you deploy a Pod on every node.
		
		or
		
	- DaemonSet ensures that all nodes can run a copy of a pod.

### Jobs :

	- How do you run pods
	
		or
		 
	- Each job creates one or more jobs
	
	Types of jobs :
	
		- Jobs  ( Run to completion )
		- CronJobs ( Shcheuled )
		
### Services :

	- A service is a grouping of pods that running on the clustter.
	
	Types of services :
		- ClusterIp
		- Node Port
		- Load Balancer
		
### ConfigMaps
	
	- How do we make containerized apps portable ??
	
### Deployments:

	- Imagine , we are upgrading your application from V1 to V2
		- Upgrade with zero time
		- Update sequentially , One after other
		- Pause and Reduce upgrade process
		- Rollback upgrade to previous stable release
		
	- Typef od Deployments
		1. Recreate ( remove and deploy )
			
			  strategy:
    				type: Recreate
				
			link : https://github.com/learn-with-devops/devops/tree/master/k8s
			
		2. Rolling Update
		
			kubectl set image deploy nginx-deployment nginx-container=nginx:latest --record.  // Update the image and record it for rollback
			kubectl rollout history deployment/nginx-deployment. // list out the rollout history
			
			kubectl rollout undo deployment/nginx-deployment.   // undo the update
			
		   Note : (Readiness Probe. -- > to make zero downtime of deployment) 
			
				https://medium.com/platformer-blog/enable-rolling-updates-in-kubernetes-with-zero-downtime-31d7ec388c81
			
		3. Canary
		4. Blue / Green

### Replication Controller (old) / Replica set (set) :
	
	- How can you ensure there is a 3 pod instances ... example 3 pods need to run at any point of time.
	
### Secrets : 
	
	- Kubernetes object to handle small amount of Data.
	
### Notes :

- Validate the k8s manifest file.
	
		kubectl create --validate=true -f file.json
	
- Run the manifest file in Dry Run mode

		kubectl apply --validate=true --dry-run=true --filename=nginx-run.yaml
	
	
