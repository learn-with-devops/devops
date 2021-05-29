import boto3

data = boto3.client('ec2')

servers = data.describe_instances(Filters=[
    {'Name': 'tag:Name', 'Values': ['kalyan1']}])

instance_list = []
public_instances_running =[]
t = {}
for i in servers['Reservations']:
    for inst_id in i['Instances']:
        t[inst_id['InstanceId']] = {
            'Public_IP': inst_id.get('PublicIpAddress'),
            'Private_IP': inst_id['PrivateIpAddress'],
            'Server_Type': inst_id['InstanceType'],
            'Key_Name': inst_id['KeyName'],
            'Instance_State': inst_id['State']['Name']
        }
        instance_list.append(inst_id['InstanceId'])

        if inst_id['State']['Name'] == 'running' and inst_id.get('PublicIpAddress') is not None:
            public_instances_running.append(inst_id['InstanceId'])

# Stop the Instances
print("Stopping the following Public Instances")
print(public_instances_running)
data.stop_instances(InstanceIds=public_instances_running)


# print(instance_list)
# # print(t)
# print(public_instances_running)


--------------------------------------------------------

## Onother way 

import json
import boto3

region = 'us-east-1'

ec2 = boto3.client('ec2', region_name=region)

def get_instance_ids(instance_names):

    all_instances = ec2.describe_instances()
    
    instance_ids = []
    
    # find instance-id based on instance name
    # many for loops but should work
    for instance_name in instance_names:
        for reservation in all_instances['Reservations']:
            for instance in reservation['Instances']:
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name' \
                            and tag['Value'] == instance_name:
                            instance_ids.append(instance['InstanceId'])
                            
    return instance_ids

def lambda_handler(event, context):
    
    instance_names = event["instances"].split(',')
    action = event["action"]

    instance_ids = get_instance_ids(instance_names)

    print(instance_ids)

    if action == 'Start':
        print("STARTing your instances: " + str(instance_ids))
        ec2.start_instances(InstanceIds=instance_ids)
        response = "Successfully started instances: " + str(instance_ids)
    elif action == 'Stop':
        print("STOPping your instances: " + str(instance_ids))
        ec2.stop_instances(InstanceIds=instance_ids)
        response = "Successfully stopped instances: " + str(instance_ids)
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
