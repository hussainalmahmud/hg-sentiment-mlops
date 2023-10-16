## Get endpoints in current region
import boto3

# Create a SageMaker client
sagemaker_client = boto3.client('sagemaker', region_name='us-east-1')

# List endpoints
response = sagemaker_client.list_endpoints()

# Print endpoint names
for endpoint in response['Endpoints']:
    print(endpoint['EndpointName'])