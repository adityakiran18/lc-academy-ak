import random
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import tiktoken

load_dotenv()
#############################################
ds_resume = r"D:\Code\ak\career_resumes_repo\industry_2025\1-page resume\neonit\resume_ds_exp.pdf"
ai_resume = r"D:\Code\ak\career_resumes_repo\industry_2025\1-page resume\elongated\ai-llm resume\ak_resume_2page.pdf"

GMAIL_USER = "adityakiran.91@gmail.com"
GMAIL_APP_PASSWORD = os.environ.get("MY_GMAIL_PASS")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)
##############################################
def generate_email_content(recruiter_email, role_name):
    """Uses Gemini to draft a personalized email body."""
    
    system_msg = "Extract first name from email for a greeting. Output ONLY the name string."
    user_prompt = f"""Target: {recruiter_email}
    Rules:
    1. If Indian name found, return it.
    2. If generic (HR/Info), return 'Recruiter'.
    3. If unsure, return the username.
    4. One word only. No intro."""    

    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=user_prompt)
    ]

    response = llm.invoke(messages)
    recruiter_name = response.content.strip()
        
    body = f"""
    <html>
        <body>
            Hi {recruiter_name}!<br>
            &nbsp;&nbsp;&nbsp;&nbsp;I have a very strong profile in ML/AI along with a PhD in Data Science. 
            I have over 8yrs experience building production-grade AI/ML solutions. 
            I am very excited about your recent posting for <b>{role_name}</b>. 
            It is an excellent fit for my profile. <b>And I meet all the required qualifications.</b>

            <p>Please review my <b>attached resume</b> and pass it on to the hiring manager.</p>

            <p>I am on an H1B visa. I have an employer who is sponsoring my visa. 
            So I am also open to working as a C2C contractor. 
            Please contact me at 312-804-9490 if you like my resume.</p>

            <p>Looking forward to hearing from you,<br>
            Aditya</p>
        </body>
    </html>
    """
    return body


def send_recruiter_email(recruiter_email, role_name, resume_path):
    # Draft the body
    email_body = generate_email_content(recruiter_email, role_name)
    
    # Create the email container
    msg = EmailMessage()
    msg['Subject'] = f"Excellent resume for {role_name}"
    msg['From'] = GMAIL_USER
    msg['To'] = recruiter_email
    msg.add_alternative(email_body, subtype="html")

    # Attach the PDF
    try:
        with open(resume_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(resume_path)
            msg.add_attachment(
                file_data,
                maintype='application',
                subtype='pdf',
                filename=file_name
            )
    except FileNotFoundError:
        print(f"❌ Resume not found at: {resume_path}")
        return False

    # Send via Gmail SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
        print(f"Yay! Email successfully sent to {recruiter_email} for {role_name}")
        return True
    except Exception as e:
        print(f"Sorry! Failed to send email to {recruiter_email}: {e}")
        return False

def get_wait_time(tlow=20, thigh=40):
    wait_time = random.randint(tlow, thigh)
    return wait_time

##############################################

def count_token(text, model="gpt-4o") -> int:
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)
