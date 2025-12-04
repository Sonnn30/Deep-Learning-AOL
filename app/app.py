import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
import json


model = tf.keras.models.load_model("model_restnet.keras")

with open('labels.json', 'r') as f:
    class_label = json.load(f)


def predict_input(img):
    img = img.resize((224, 224))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0]
    idx = np.argmax(pred)

    return class_label[idx]


demo = gr.Interface(
    fn=predict_input,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label()

)


demo.launch()