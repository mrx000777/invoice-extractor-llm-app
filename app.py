from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import json

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini 1.5 Flash Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Prepare uploaded image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Get Gemini response
def get_gemini_response(system_prompt, image, user_prompt):
    response = model.generate_content([system_prompt, image[0], user_prompt])
    return response.text

# Streamlit UI
st.set_page_config(page_title="Invoice Field Extractor - Gemini 1.5 Flash")
st.header("🧾 Invoice Field Extractor using Gemini 1.5 Flash")

# User input prompt
user_input = st.text_input(
    "🔍 What do you want to extract from the invoice?",
    placeholder="e.g., Subtotal, Tax Amount, Vendor Name, Invoice Date"
)

# Upload invoice image
uploaded_file = st.file_uploader("📤 Upload invoice image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

# System prompt: forces Gemini to extract ONLY what user asks
input_prompt = """
You are an expert invoice parser. The user will request specific information from an uploaded invoice.

⚠️ Your task is to ONLY extract the exact field the user asks for.

❗Do NOT include extra fields or explanation.
If the field is not found, respond with:
{ "<field>": null }

Always return the result strictly in JSON format like:
{ "<field>": "<value>" }
"""

# Action button
if st.button("🔎 Extract Info"):
    if uploaded_file and user_input:
        try:
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, f"Extract this field: {user_input}")
            st.subheader("✅ Extracted Field:")
            st.code(response, language="json")

            # Optional download button
            st.download_button(
                label="📥 Download JSON",
                data=response,
                file_name="extracted_field.json",
                mime="application/json"
            )
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please upload an image and type a field to extract.")
