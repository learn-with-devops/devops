## Deployment

deployment types are :

  1. Recreate -> create app-B instances once app-A instences completley down.( there is a down time )
  
  2. Rolling Update - > default update startagy from k8s..once App-B instance got deployed then it will add to the pool and App-A instance will remove from there.
  
  3. Canary -> out of 10 instances it will deploy 2 instances and will verify/test the things and deploy remaing if all or fine.
  
  4. Blue / Green Deployment --> deploy the same number of instances paralally and will switch the traffic once all are working fine.
