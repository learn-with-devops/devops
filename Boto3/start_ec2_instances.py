## Start all Ec2 Instances in a region

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




## Start EC2 instances based on tags

import boto3
import time

ec = boto3.client('ec2')

inst = ec.describe_instances(Filters=[{'Name': 'tag:name', 'Values': ['backup']}])
#print(inst)

instancelist = []
for i in inst['Reservations']:
  for st in i['Instances']:
#    print(st['InstanceId'], st['PublicIpAddress'])
    instancelist.append(st['InstanceId'])

#print(instancelist)

print("----------------- Ec2 Instance Status before Stopping-----------------")
for ins in instancelist:
	print(ins, st['State']['Name'])

ec.stop_instances(InstanceIds = instancelist)

# Sleep for 15 mins
time.sleep(20)

print("----------------- Ec2 Instance Status After Stopping-----------------")
for ins1 in instancelist:
	print(ins1, st['State']['Name'])
