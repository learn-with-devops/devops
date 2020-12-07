import boto3

data = boto3.client('ec2', region_name='us-east-2')

servers = data.describe_instances()

instance_list = []
public_instances_running =[]
t = {}
for i in servers['Reservations']:
    for inst_id in i['Instances']:
        instance_list.append(inst_id['InstanceId'])

print(instance_list)
# print(instance_list)
# # print(t)
# print(public_instances_running)

