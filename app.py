from transformers import pipeline 
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

demo = gr.Interface(fn=predict, inputs="textbox", outputs="text", 
                   title="Text Summarization",
                   description="Enter text to get a summary.")

demo.launch()
