### Statefulset

A StatefulSet is the Kubernetes controller used to run the stateful application as containers (Pods) in the Kubernetes cluster. StatefulSets assign a sticky identity—an ordinal number starting from zero—to each Pod instead of assigning random IDs for each replica Pod. A new Pod is created by cloning the previous Pod’s data. If the previous Pod is in the pending state, then the new Pod will not be created. If you delete a Pod, it will delete the Pod in reverse order, not in random order. For example, if you had four replicas and you scaled down to three, it will delete the Pod numbered 3.

Ref Link: https://loft.sh/blog/kubernetes-statefulset-examples-and-best-practices/
Ref Link: https://github.com/MithilShah/kubernetes-course/tree/master/kubernetes_statefulsets

### Deployments vs StatefulSets vs DaemonSets.

	Deployment - You specify a PersistentVolumeClaim that is shared by all pod replicas. In other words, shared volume.

			The backing storage obviously must have ReadWriteMany or ReadOnlyMany accessMode if you have more than one replica pod.

	StatefulSet - You specify a volumeClaimTemplates so that each replica pod gets a unique PersistentVolumeClaim associated with it. In other words, no shared volume.

			Here, the backing storage can have ReadWriteOnce accessMode.

			StatefulSet is useful for running things in cluster e.g Hadoop cluster, MySQL cluster, where each node has its own storage.

	DaemonSets - DaemonSet is a controller similar to ReplicaSet that ensures that the pod runs on all the nodes of the cluster. If a node is added/removed from a cluster, DaemonSet automatically adds/deletes the pod.

### Declare the sidecar containers in a Pod.

A sidecar is just a container that runs on the same Pod as the application container, because it shares the same volume and network as the main container, it can “help” or enhance how the application operates. Common examples of sidecar containers are log shippers, log watchers, monitoring agents among others.

		apiVersion: v1
		kind: Pod
		metadata:
		  name: bookings-v1-b54bc7c9c-v42f6
		  labels:
		    app: demoapp
		spec:
		  containers:
		  - name: bookings
		    image: banzaicloud/allspark:0.1.1
		    ...
		  - name: istio-proxy
		    image: docker.io/istio/proxyv2:1.4.3
		    lifecycle:
		      type: Sidecar

### Commands
 List out all the server resources

	 kubectl describe nodes | grep 'Name:\|  cpu\|  memory'
	 
### Pod creation restriction
	Restrict pod creation to specific node with NodeSelector ( we can use constraints and nodeName as well)
	https://quip.com/2DLOANcntXHO/Restrict-Pod-creation
	 
### Taints and Tolarations 

	spec:
           tolerations:
           - effect: NoSchedule
             key: key
             operator: Equal
             value: epam
	     
### Pod Eviction | Removing worker Node

When administering your Kubernetes cluster, you will likely run into a situation where you need to delete pods from one of your nodes. You may need to debug issues with the node itself, upgrade the node, or simply scale down your cluster.

Deleting pods from a node is not very difficult, however there are specific steps you should take to minimize disruption for your application. Be sure to fully read and understand each step before executing any commands to ensure no mistakes happen that could lead to downtime.

Remove Node from cluster :-

	1.  Perform drain operation in that node to kill the pods in present folder and start it in different nodes.

	    kubectl cordon <nodeName>
	    
	    cordon :  Means, It will mark as un-scheduled

	Note : When you darin the node, you need to ignore the daemon sets and remove local storage like below : 

	> kubectl drain <node-name> --ignore-daemonsets --delete-local-data --force

	2. If you want to add the node back to cluster then uncordon that.

	> kubectl uncordon <nodeName>
	
	    uncordon : Means, It will mark as schduled

	3. Remove workernode from cluster

	> kubectl delete node <node name>



## Volumes
	- PV , PVC ( Static )  and Storage Class ( Dynamic )
Notes: 
	- PV is created cluster level and pvc belong to namespace level
	- With Storage class you can automate the PV creation by specifing only pv claim.
	- If you declare PV then PVC you need to use the same labels, storage type, access modes and resources ( Some times if the avilable resources are more than u requested also fine ).
	
		---
		## Create a PV with your NFS shared folder.
		apiVersion: v1
		kind: PersistentVolume
		metadata:
		  name: nfs-pv-hpcc
		spec:
		  capacity:
		    storage: 65Gi
		  volumeMode: Filesystem
		  accessModes:
		    - ReadWriteMany
		  persistentVolumeReclaimPolicy: Recycle
		  storageClassName: nfs-sc-hpcc
		  mountOptions:
		    - hard
		    - nfsvers=4.1
		  nfs:
		    path: /data            ## Shared folder of NFS server
		    server: 52.118.191.60  ## Name of the NFS server.

		---
		## Create a PVC from PV.
		apiVersion: v1
		kind: PersistentVolumeClaim
		metadata:
		  name: nfs-pvc-hpcc
		spec:
		  accessModes:
		    - ReadWriteMany
		  storageClassName: nfs-sc-hpcc
		  resources:
		    requests:
		      storage: 65Gi
	
## Name Spaces

we have 4 default namespaces creating by k8s: 

	default The default namespace for objects with no other namespace
	kube-system The namespace for objects created by the Kubernetes system
	kube-public This namespace is created automatically and is readable by all users (including those not authenticated). This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a requirement.
	kube-node-lease This namespace for the lease objects associated with each node which improves the performance of the node heartbeats as the cluster scales.

## Liveness |Readiness |startup probes

	the *liveness probe* will restart a container when it becomes unresponsive *and* the *readiness probe* is used to decide when a container is *ready* to start *or* stop accepting traffic

## Startup probe:

	Legacy applications take time to start and kubectl will kill the pod and start new one. So, to avoid this use startup probe
	The startup probe is only called during startup and is used to determine when the container is ready to accept requests. If a startup probe is configured, the liveness and readiness checks are disabled until the startup probe succeeds. If a startup probe exceeds the configured failureThreshold without succeeding, the container is killed and restarted, subject to the pod's restartPolicy, a behaviour analogous to the liveness probe.



## Adopter Container :  ( like Side cart container )


	The *Adapter container* is a simple express node server that reads from the location /var/log/file.log and produces JSON format. Let's implement a simple project to understand this pattern. The *Adapter container* is a simple express API that serves these logs as a JSON response.


## Headless pod ( with no load balancer, only cluster IP )

	A *headless* service is a service with a service IP but instead of load-balancing it will return the IPs of our associated *Pods*. This allows us to interact directly with the *Pods* instead of a proxy. It's as simple as specifying None for .

## StatefulSets ( It will store the app information permanentley ) : 

	StatefulSet is a Kubernetes resource used to manage stateful applications. It manages the deployment and scaling of a set of Pods, and provides guarantee about the ordering and uniqueness of these Pods.
	
	Note: 
		Every replica of a stateful set will have its own state, and each of the pods will be creating its own PVC(Persistent Volume Claim). So a statefulset with 3 replicas will create 3 pods, each having its own Volume, so total 3 PVCs.

	Ex: 
			apiVersion: apps/v1
			kind: StatefulSet
			metadata:
			  name: counter
			spec:
			  serviceName: "counter-app"
			  selector:
			    matchLabels:
			      app: counter
			  replicas: 1 
			  template:
			    metadata:
			      labels:
				app: counter
			    spec:      
			      containers:
			      - name: counter
				image: "kahootali/counter:1.1"  
				volumeMounts:
				- name: counter
				  mountPath: /app/      
			  volumeClaimTemplates:
			  - metadata:
			      name: counter
			    spec:
			      accessModes: [ "ReadWriteMany" ]
			      storageClassName: efs
			      resources:
				requests:
				  storage: 50Mi


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
	 -> configMaps ( v1 apiVersion )



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
	
	
### HPA and VPA
Ref : https://medium.com/nerd-for-tech/autoscaling-in-kubernetes-hpa-vpa-ab61a2177950#:~:text=Unlike%20Horizontal%20Pod%20Autoscaler%20(%20HPA,suitable%20CPU%20and%20Memory%20attributes.

	apiVersion: autoscaling/v1
	kind: HorizontalPodAutoscaler
	metadata:
	  name: k8s-autoscaler
	spec:
	  maxReplicas: 10
	  minReplicas: 2
	  scaleTargetRef:
	    apiVersion: apps/v1
	    kind: Deployment
	    name: k8s-autoscaler
	  targetCPUUtilizationPercentage: 50
