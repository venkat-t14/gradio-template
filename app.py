from fastapi import FastAPI, Depends, Body
import gradio as gr
from utils import test_fn

main_app = FastAPI(redoc_url=None, docs_url=None)


@main_app.get("/predict")
async def predict():
    return test_fn()


demo = gr.Interface(
    fn=test_fn,
    inputs=[
        gr.Textbox(label="Client ID", value="91648"),
        gr.Textbox(
            label="Product IDs in the Menu (comma-separated)", value="2710, 2882"
        ),
        gr.Number(label="Date", value="13"),
        gr.Number(label="Month", value="6"),
        gr.Number(label="Year", value="2023"),
    ],
    outputs=gr.HTML(
        label="Result",
    ),
    theme="sudeepshouche/minimalist",
    allow_flagging="never",
)


main_app = gr.mount_gradio_app(main_app, demo, path="/")