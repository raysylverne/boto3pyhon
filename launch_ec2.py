import boto3


ec2 = boto3.client('ec2')
response = ec2.run_instances(ImageID='ami-082489fc6312797a6',
                             InstanceType='t2.micro',
                             MinCount=1,
                             MaxCount=2)