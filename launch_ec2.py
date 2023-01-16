import boto3

''' 
ec2 = boto3.client('ec2')
response = ec2.run_instances(ImageID='ami-082489fc6312797a6', 
                             InstanceType='t2.micro',
                             MinCount=1,
                             MaxCount=1)


for instance in response['Instances']:
    print(instance['InstanceID'])
'''
client = boto3.client('ec2')
resp = client.run_instances(ImageID='ami-0b5eea76982371e91',
                             InstanceType='t2.micro',
                             MinCount=1,
                             MaxCount=1)

for instance in resp['Instances']:
    print(instance['InstanceID'])