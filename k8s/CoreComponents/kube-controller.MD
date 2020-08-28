## Controller


The Kubernetes controller manager is a daemon that embeds the core control loops shipped with Kubernetes. 
In Kubernetes, a controller is a control loop that watches the shared state of the cluster through the 
apiserver and makes changes attempting to move the current state towards the desired state. 
Examples of controllers that ship with Kubernetes today are the replication controller, 
endpoints controller, namespace controller, and serviceaccounts controller.


Basically, a controller watches the desired state of the objects it manages and watches their current state through the API server. 
If the current state of the objects it manages does not meet the desired state, then the control loop takes corrective steps to 
make sure that the current state is the same as the desired state.


## Controller Types

  - Node Controller
  - NameSpace Controller
  - Replica Controller
  - Deployement
  - EndPoint
  - CronJob
  - Job
  - Stateful
  - Service account
  - PV Protection
  
Notes : 

  - Node Controller
  
      It is monitor the health of nodes with the help of Kube-API-Server.
      
          - It checks the status of nodes every 5 seconds 
                    NODE MONITOR PERIOD = 5S
          - If node checks failed continuosly 40 seconds then it will monitor as UnReachable.
                    NODE MONITOR GRACE PERIOD = 40S
          - It waits 5mins to comeback to normal position.Else it will remove the node from cluster and provisions the nodes to the healty servers.
                    POD EVICTION TIMEOUT = 5M
