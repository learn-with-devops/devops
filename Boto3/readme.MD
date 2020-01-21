## Python Boto3 for automating AWS infrastructure


### Create a Session with your AWS account

    There are 3 ways to get your AWS session with Boto3
    
        1. **HardCoding** the Credentials
                 root_session = boto3.session.Session(aws_access_key_id="sJHSDJFGDXC" , aws_secret_key_id="LKSDHFJKDHFXJDXH")
        2. Using **AWS Configure**
                 root_session = boto3.session.Session(profile_name="default")
        3. Exporting Programatic access keys as **environmant variable**.
        
### Connect with Any Service ( EC2 ) :

    We can connect any services from AWS console in 2 ways.
    
        1. resource Method
        2. Client Method
        
        ------------------------------------------------------------------------------------------------                                                                                               
       |         Resource                            |    .            Client                           |
        ------------------------------------------------------------------------------------------------
        1. High level Method ( only high level          1. Low level Method (All the operations will be
           operations are avilable )                       with client method )
        
        2. Final Output will be Object.                 2. Final Output will be Dict and List.
        
        
        Note : Meta ( If you are not able to find the options with Resource then META is helpful for entering to the client from resource.
