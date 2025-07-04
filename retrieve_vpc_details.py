# This script connects to AWS using Boto3, searches for a VPC by its "Name" tag,
# and prints detailed information about the VPC in JSON format.
# It is useful for inspecting VPC configurations by tag name within a specific region.

#Requirements:
# Confiure AWS CLI authentication credential setup via "aws configure" in the terminal
# make sure to install boto3 using "pip install boto3"

# Import required libraries:
# 'json' to format and print the output nicely
# 'boto3' is the AWS SDK for Python that allows you to interact with AWS services



import json, boto3

# Define the AWS region where your VPC is located
region = 'eu-west-2' # change this to your own zone here if different

# Define the name of the VPC you want to find
vpc_name = 'vpc-1' #change this to your own vpc here if different

# Create an EC2 resource object for interacting with EC2 resources in the specified region
ec2 = boto3.resource('ec2', region_name=region)

# Create an EC2 client object to make low-level AWS service calls
client = boto3.client('ec2')

# Set up filters to find VPCs with a specific "Name" tag (e.g. tag:Name = vpc-1)
filters = [{'Name': 'tag:Name', 'Values': [vpc_name]}]

# Use the filters to get a list of VPCs that match the given name
vpcs = list(ec2.vpcs.filter(Filters=filters))

# Loop through each matching VPC (in case there are multiple with the same name tag)
for vpc in vpcs:
    # Use the EC2 client to get detailed information about the VPC by its ID
    response = client.describe_vpcs(VpcIds=[vpc.id])

    # Print the VPC information in a nicely formatted JSON structure
    print(json.dumps(response, sort_keys=True, indent=4))




