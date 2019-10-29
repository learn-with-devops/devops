import boto3
ec2 = boto3.client('ec2')

inst = ec2.describe_instances()

# print(type(inst))

for i in inst['Reservations']:
    for t in i['Instances']:
       #  print(t['PublicIpAddress'],t['Monitoring'])
       #  print(t['PublicIpAddress'])
       f = open('enventory','a+')
       f.write(t['PublicIpAddress'] + '\n')
       f.close()
