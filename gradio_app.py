# from transformers import pipeline 
import gradio as gr

# model = pipeline("summarization")

# def predict(prompt):
#     summary = model(prompt)[0]["summary_text"]
#     return summary

# demo = gr.Interface(fn=predict, inputs="textbox", outputs="text", 
#                   title="Text Summarization",
#                   description="Enter text to get a summary.")

# demo.launch()


import boto3

# Create a SageMaker client
sagemaker_client = boto3.client('sagemaker', region_name='us-east-1')

# List endpoints
response = sagemaker_client.list_endpoints()

# Print endpoint names
for endpoint in response['Endpoints']:
    print(endpoint['EndpointName'])