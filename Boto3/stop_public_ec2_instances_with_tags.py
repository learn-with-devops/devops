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
