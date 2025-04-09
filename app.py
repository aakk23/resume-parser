import streamlit as st
import os
from resume_parser_v05 import parse_resume

st.set_page_config(page_title="Resume Parser", layout="centered")

st.title("📄 Resume Parser")
st.markdown("Upload one or more **PDF resumes** to extract key information like Name, Email, Phone, Social Links, and Skills.")

uploaded_files = st.file_uploader(
    "Upload PDF resumes", 
    type=["pdf"], 
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        with st.spinner(f"🔍 Processing: {uploaded_file.name}"):
            # Save file to disk temporarily
            temp_path = f"temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())

            try:
                result = parse_resume(temp_path)

                st.success(f"✅ Parsed: {uploaded_file.name}")
                st.json(result)

            except Exception as e:
                st.error(f"❌ Error processing {uploaded_file.name}: {e}")

            finally:
                os.remove(temp_path)
