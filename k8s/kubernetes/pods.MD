## POD

- List out the Pods

      kubectl get pods / kubectl get po
  
- List out the Pods complete information
  
      kubectl get pods -o wide
  
- Create a pod from manifest file
  
      kubectl create -f filename.yml
  
- List out the pod configuration in YAML format
  
  
      kubectl get pod nginx-pod -o yaml
  
- List out the details of POD
  
      kubectl describe pod nginx-pod
  
- Test the Pod able to reach/not
  
      ping <pod IP>.  // Do it in POD master server
  
- Jump into the pod container
      
      kubectl exec -it <podname> -- /bin/sh
  
  
