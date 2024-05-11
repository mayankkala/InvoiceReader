from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import io
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_output(input, image, prompt):
    response=model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config('Invoiceibot')
st.header("Now read your Invoice with AI")
input_text=st.text_input("Write your question here...")
uploaded_file=st.file_uploader("Upload Invoice here", type=["jpg", "jpeg", "png"])
img=""

if uploaded_file is not None:
    img= Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image.", use_column_width=True)

submit_button=st.button("Submit your invoice")    

input_prompt="""
You are an expert in understanding invoices. We will upload a a image as invoice
and you will have to answer any questions based on the uploaded invoice image. Make sure you only answer what's asked.
"""
if submit_button:
    image_bytes = input_image_details(uploaded_file)
    response=get_gemini_output(input_prompt, image_bytes, input_text)
    st.subheader("The response is: ")
    st.write(response)




