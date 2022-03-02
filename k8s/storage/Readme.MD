PV, PVC and Storage Classes :-
------------------------------

Key Points:
-----------
- PV is created cluster level and pvc belong to namespace level. 
- With Storage class you can automate the PV creation by specifing only pv claim. 
- If you declare PV then PVC you need to use the same labels, storage type, access modes and resources ( Some times if the avilable resources are more than u requested also fine ).

Persistent Volumes:
--------------------

A PersistentVolume (PV) is a storage resource in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes.

      ---
      ## Create a PV with your NFS shared folder.
      apiVersion: v1
      kind: PersistentVolume
      metadata:
        name: nfs-pv-hpcc
      spec:
        capacity:
          storage: 1000Gi # Specify the size of Volume you created
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
          server: 10.248.0.12  ## Name of the NFS server.


Persistent Volume Claims:
--------------------------

A persistent volume claim (PVC) is a request for storage by a user from a PV. Claims can request specific size and access modes (e.g: they can be mounted once read/write or many times read-only).

      ---
      ## Create a PVC from PV.
      apiVersion: v1
      kind: PersistentVolumeClaim
      metadata:
        name: nfs-pvc-hpcc
        namespace: hpcc # Choose your own Namespace 
      spec:
        accessModes:
          - ReadWriteMany
        storageClassName: nfs-sc-hpcc
        resources:
          requests:
            storage: 1000Gi


Application Deployment with PVC :
---------------------------------

Deploying sample Nginx application with "/usr/share/nginx/html/" path.

      ---
      apiVersion: v1
      kind: Pod
      metadata:
        name: nginx-pv-pod
      spec:
        volumes:
          - name: nginx-pv-storage
            persistentVolumeClaim:
              claimName: nfs-pvc-hpcc   # This should be exactly match with PVC name. 
        containers:
          - name: nginx
            image: nginx
            ports:
              - containerPort: 80
                name: "nginx-server"
            volumeMounts:
              - mountPath: "/usr/share/nginx/html"
                name: nginx-pv-storage


Dynamic Provisioning with StorageClasses:
-----------------------------------------

This provisioning is based on StorageClasses, the PVC must request a storage class and the administrator must have created and configured that class for dynamic provisioning to occur.

Volume implementations are configured through StorageClass resources.
If you set up a Kubernetes cluster on GCP, AWS, Azure, or any other cloud platform, a default StorageClass creates for you which uses the standard persistent disk type.

Note: If you create a PVC, automatically PV and Volume will create in backend.

          ---
          apiVersion: v1
          kind: PersistentVolumeClaim
          metadata:
            name: anand-hh-pvc
            labels:    # It will create a Volume automatically based on Storage class Name.
              billingType: "hourly"
              region: jp-osa
              zone: osa21
          spec:
            accessModes:
              - ReadWriteOnce
            resources:
              requests:
                storage: 132Gi
            storageClassName: ibmc-vpc-block-5iops-tier
            
            

Creating a PV from awsElasticBlockStore :
-----------------------------------------

Before you can use an EBS volume with a Pod, you need to create it.

      aws ec2 create-volume \
      --availability-zone=eu-west-1a \
      --size=100 \
      --volume-type=gp2

Usase :

      apiVersion: v1
      kind: PersistentVolume
      metadata: 
        name: test-volume
      spec: 
        accessModes: 
          - ReadWriteOnce
        awsElasticBlockStore: 
          fsType: ext4
          volumeID: ~
        capacity: 
          storage: 100Gi
        storageClassName: ebs-disk
