import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
inst = ec2.describe_instances(Filters=[
    {'Name': 'tag:Name', 'Values': ['kalyan1']}])
instances = []
for i in inst['Reservations']:
  for st in i['Instances']:
    instances.append(st['InstanceId'])
    
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
    
