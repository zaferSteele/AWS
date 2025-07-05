# This script uses Boto3 to create a new security group in AWS EC2.
# It retrieves the first VPC, creates a security group, and adds inbound rules
# to allow HTTP (port 80) and SSH (port 22) traffic from any IP address.

#Requirements:
# Confiure AWS CLI authentication credential setup via "aws configure" in the terminal
# make sure to install boto3 using "pip install boto3"

# Import required libraries:
# 'json' to format and print the output nicely
# 'boto3' is the AWS SDK for Python that allows you to interact with AWS services


import boto3

# Create an EC2 client using Boto3
ec2 = boto3.client('ec2')

# Retrieve information about available VPCs (Virtual Private Clouds)
response = ec2.describe_vpcs()

# Get the ID of the first VPC in the list; if none found, use empty string
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

# Create a new security group in the selected VPC
response = ec2.create_security_group(
    GroupName='zafer_security_group',        # Name of the new security group
    Description='Zafer_sg',                  # Description of the security group
    VpcId=vpc_id                              # VPC in which to create the security group
)

# Store the ID of the newly created security group
security_group_id = response['GroupId']

# Define rules to allow incoming traffic on specific ports (ingress rules)
data = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',                 # Protocol: TCP
            'FromPort': 80,                      # Allow incoming traffic starting at port 80
            'ToPort': 80,                        # ... and ending at port 80 (HTTP)
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}] # Allow from any IP address
        },
        {
            'IpProtocol': 'tcp',                 # Protocol: TCP
            'FromPort': 22,                      # Allow incoming traffic starting at port 22
            'ToPort': 22,                        # ... and ending at port 22 (SSH)
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}] # Allow from any IP address
        },
    ]
)

# Print confirmation that ingress rules were successfully applied
print('Ingress Successfully Set %s' % data)

# Print the security group ID for reference
print(security_group_id)




