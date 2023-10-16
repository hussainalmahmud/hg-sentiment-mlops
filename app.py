from fastapi import FastAPI, HTTPException
import boto3
app = FastAPI()

# Initialize SageMaker runtime client
sagemaker_runtime = boto3.client('sagemaker-runtime')

ENDPOINT_NAME = "sagemaker-studio-hg-epc-2023-10-16-02-39-58"

@app.post("/predict/")
async def predict(data: str):
    # Make a call to the SageMaker endpoint
    try:
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType="text/plain",
            Body=data
        )
        # Decode the response and return it
        prediction = response['Body'].read().decode('utf-8')
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
