## Scheduling

### Manual Scheduling

    we can schedule manually by specifing the "nopeName" in manifest file...
    There is no way to use kubectl to update the pod once its created.But, you can use with the API to pass.
    
    ex: 
       spec:
        nodeName: server02
