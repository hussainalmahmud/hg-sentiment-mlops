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

# hugging-face-mlops-demo

## get Sagemaker endpoints
```
 aws sagemaker list-endpoints --region your-region-name
```


Run the FastAPI application using:
```
uvicorn filename:app --reload
```

Using a Web Browser:
```
If you're sending a GET request, you can simply open a web browser and navigate to the endpoint URL 
(e.g., http://localhost:8000/predict/). However, in our example, we defined a POST endpoint, so we'll need another method.
```

Using curl:
You can use the curl command from your terminal:
```
curl -X POST "http://localhost:8000/predict/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":\"YourDataHere\"}"
```



## To use git inside Cloud9
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com
```
After doing this, you may fix the identity used for this commit with:
```
    git commit --amend --reset-author
```