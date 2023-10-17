import os
from fastapi import FastAPI, HTTPException
import uvicorn
import boto3
import json
from fastapi import FastAPI, HTTPException

app = FastAPI()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
ENDPOINT_NAME = os.getenv('ENDPOINT_NAME')

print("AWS Access Key ID:", AWS_ACCESS_KEY_ID)
print("AWS Secret Access Key:", AWS_SECRET_ACCESS_KEY)
print("Endpoint Name:", ENDPOINT_NAME)

runtime = boto3.client("sagemaker-runtime",
                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


@app.get("/")
def read_root():
    return {"Welcome": "This is the FastAPI application!"}
    
@app.get("/check-env-vars/")
def check_env_vars():
    return {
        "AWS_ACCESS_KEY_ID": os.getenv('AWS_ACCESS_KEY_ID') or "Not Found",
        "AWS_SECRET_ACCESS_KEY": "Hidden for security purposes",
        "ENDPOINT_NAME": os.getenv('ENDPOINT_NAME') or "Not Found"
    }

@app.post("/predict/")
async def predict(message: str):
    try:
        content_type = "application/json"
        data = {
            "inputs": message
        }
        
        sagemaker_response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType=content_type,
            Body=json.dumps(data)
        )
        prediction = sagemaker_response['Body'].read().decode()
        return json.loads(prediction)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host='0.0.0.0', port=8080, log_level='info')
