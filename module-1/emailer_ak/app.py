import streamlit as st
from dotenv import load_dotenv
import time
from utils import (
    ds_resume, 
    ai_resume,
    send_recruiter_email,
    get_wait_time,
)

load_dotenv()

st.title("🚀 AKY's AI-emailer")

# Inputs
role_type = st.selectbox("Select Resume Type", ["Data Science", "AI/ML"])
input_data = st.text_area(
    "Enter Roles & Emails (Format: Role, Email - one per line)", 
    placeholder="""Senior Data Scientist, recruiter@dell.com \n Data Scientist, jobs@lbl.gov"""
)

if st.button("Send Emails"):
    # Parse the text area
    lines = [
        [part.strip() for part in line.rsplit(",", 1)] 
        for line in input_data.split("\n") 
        if "," in line
    ]
    
    resume_path = ds_resume if role_type == "Data Science" else ai_resume
    
    progress_bar = st.progress(0)
    for i, (role, email) in enumerate(lines):
        
        clean_email = email.strip()
        clean_role = role.strip()
        st.write(f"Sending to {clean_email} for {clean_role}...")
        
        success = send_recruiter_email(clean_email, clean_role, resume_path)
        
        if success:
            st.write(f"Sent to {clean_email}")
        else:
            st.write("Error: The email couldn't be sent")

        # Update progress
        progress_bar.progress((i + 1) / len(lines))
        
        if i < len(lines) - 1:
            wt = get_wait_time()
            st.info(f"Waiting {wt}s to avoid spam filters")
            time.sleep(wt)
            
    st.success("All emails sent!")