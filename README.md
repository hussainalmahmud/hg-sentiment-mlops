---
title: Demo 
emoji: 🤗
colorFrom: purple 
colorTo: purple 
sdk: gradio 
idk_version: 3.0.6 
app_file: app.py 
pinned: false 
license: cc
---
[![Sync to Hugging Face hub](https://github.com/hussainsan/hugging-face-mlops-demo/actions/workflows/main.yml/badge.svg)](https://github.com/hussainsan/hugging-face-mlops-demo/actions/workflows/main.yml)

# 🚀 FastAPI SageMaker Integration

## 📖 Overview

This application is a simple FastAPI web service that integrates with AWS SageMaker for predictions. It's designed to fetch environment variables for AWS authentication and invoke a specific SageMaker endpoint to get predictions.

## ✨ Features:

1. **🙌 Welcome Route**: Accessing the root URL (`/`) provides a welcome message indicating the service is up and running.

2. **🔍 Environment Variables Check**: The `/check-env-vars/` route allows for a quick check on the AWS environment variables. It shows if the `AWS_ACCESS_KEY_ID` and `ENDPOINT_NAME` have been set up correctly while keeping the `AWS_SECRET_ACCESS_KEY` hidden for security purposes.

3. **🔮 Prediction Route**: The `/predict/` route enables you to make prediction requests to a pre-configured SageMaker endpoint. The app interfaces with the SageMaker runtime using the provided AWS credentials, and forwards the user's input for predictions.

## ⚙️ Setup:

### 📡 Get SageMaker Endpoints

To obtain the list of SageMaker endpoints:
```
aws sagemaker list-endpoints --region your-region-name
```

### 🌍 Export Your Environment Variables

Set up the required environment variables:
```
export AWS_ACCESS_KEY_ID='YOUR_AWS_ACCESS_KEY_ID'
export AWS_SECRET_ACCESS_KEY='YOUR_SECRET_KEY'
export ENDPOINT_NAME='YOUR_ENDPOINT_NAME'
```

### 🏃 Running the FastAPI Application:

You can start the FastAPI application using the following:

```bash
uvicorn app:app --reload
uvicorn app:app --reload --port 8080
```
Or simply run:
```bash
python app.py
```

If you're using AWS Cloud9, view the running FastAPI app by navigating to:
`Tools > Preview Running Applications`.

#### 🔗 Testing the Endpoints:

- **🌐 Using a Web Browser**:
For GET requests, simply open a web browser and navigate to the endpoint URL (e.g., `http://localhost:8000/predict/`). However, our prediction endpoint requires a POST request.

- **🔧 Using curl**:
To make a POST request, use the following curl command:
```
curl -X POST "http://localhost:8000/predict/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":\"YourDataHere\"}"
```

### 🛠️ Using Git inside Cloud9:

Set your Git configuration if prompted:
```bash
git config --global user.name "Your Name"
git config --global user.email you@example.com
```
To fix the identity for a specific commit:
```bash
git commit --amend --reset-author
```

---