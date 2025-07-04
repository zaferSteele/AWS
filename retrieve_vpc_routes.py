# Script to retrieve and display the first route table from AWS EC2 in a specific region.
# Uses Boto3 to call AWS EC2's describe_route_tables API and prints the result in readable JSON format.

#Requirements:
# Confiure AWS CLI authentication credential setup via "aws configure" in the terminal
# make sure to install boto3 using "pip install boto3"

# Import required libraries:
# - json: for formatting the output in a readable way
# - boto3: the AWS SDK for Python, used to interact with AWS services
import json, boto3

# Define the AWS region where your resources are located
region = 'eu-west-2'

# Create an EC2 resource object to interact with EC2 service using higher-level methods
ec2 = boto3.resource('ec2', region_name=region)

# Create a low-level EC2 client object for direct service API calls
client = boto3.client('ec2')

# Use the client to retrieve information about all route tables in the selected region
response = client.describe_route_tables()

# Print the first route table's data in a formatted, readable JSON structure
print(json.dumps(response['RouteTables'][0], sort_keys=True, indent=4))
