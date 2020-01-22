import boto3 

#re = boto3.resource('ec2')
#print(dir(re))
print( "==================================")

ec = boto3.client('ec2')

#print(type(ec))

#print(dir(ec))

inst = ec.describe_instances()
#print(inst)

print( "==================================")

instancelist = []
for i in inst['Reservations']:
  for st in i['Instances']:
    print(st['InstanceId'])
    instancelist.append(st['InstanceId'])
print("-------------------")
print(instancelist)
ec.start_instances(InstanceIds = instancelist)
    
# print("Public IP Address : " + st['PublicIpAddress'], "Public DNS Name : " + st['PublicDnsName'], "Instance ID : " + st['InstanceId'])
# print(ec.stop_instances(InstanceIds = ['i-098d91a038f924470']))
