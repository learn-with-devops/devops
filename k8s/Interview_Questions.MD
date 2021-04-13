1. Imperative Management VS Declarative Management


      Those are two different approaches:

      Imperative Management
        kubectl create is what we call Imperative Management. On this approach you tell the Kubernetes API what you want to create, replace or delete, not how you want your K8s cluster world to look like.

      Declarative Management
        kubectl apply is part of the Declarative Management approach, where changes that you may have applied to a live object (i.e. through scale) are "maintained" even if you apply other changes to the object.


2. Pods stuck in Terminating status and delete it forcefully.

    kubectl delete pod <PODNAME> --grace-period=0 --force --namespace <NAMESPACE>
