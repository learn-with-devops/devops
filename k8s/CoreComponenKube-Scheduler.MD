
## Scheduler

    While scanning the API server (which it is continuously doing), the Kubernetes Scheduler detects that there is a new Pod without a nodeName parameter. The nodeName is what shows which node should be owning this Pod.
    The Scheduler selects a suitable node for this Pod and updates the Pod definition with the node name (though the nodeName parameter).
    The kubelet on the chosen node is notified that there is a pod that is pending execution.
    The kubelet executes the Pod, and the latter starts running on the node.


## Node selection in kube-scheduler

kube-scheduler selects a node for the pod in a 2-step operation:

    Filtering
    Scoring

The filtering step finds the set of Nodes where it's feasible to schedule the Pod. For example, the PodFitsResources filter checks whether a candidate Node has enough available resource to meet a Pod's specific resource requests. After this step, the node list contains any suitable Nodes; often, there will be more than one. If the list is empty, that Pod isn't (yet) schedulable.

In the scoring step, the scheduler ranks the remaining nodes to choose the most suitable Pod placement. The scheduler assigns a score to each Node that survived filtering, basing this score on the active scoring rules.

Finally, kube-scheduler assigns the Pod to the Node with the highest ranking. If there is more than one node with equal scores, kube-scheduler selects one of these at random.
