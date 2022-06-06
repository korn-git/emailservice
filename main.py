import smtplib
from email.message import EmailMessage
import textwrap
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000",
           "https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/sendmail/token")
async def send_email(token: str, email: str, username: str):
    receiver = email
    receiver_name = username
    wrapped_token = textwrap.wrap(token)
    msg = EmailMessage()
    msg['Subject'] = 'Your requested JWT Token'
    msg['From'] = "data-api@mea.or.th"
    msg['To'] = receiver
    msg.set_content(
        f"Dear {receiver_name},\n\nYour token is valid for 180 days.\nHere is your token:\n\n{wrapped_token[0]}\n{wrapped_token[1]}\n{wrapped_token[2]}")

    # Send the email via our own SMTP server.
    with smtplib.SMTP(host='10.110.206.200', port=25) as s:
        s.send_message(msg)


@app.get("/sendmail/info")
async def send_email(id: str, email: str, username: str):
    receiver = email
    receiver_name = username
    requested_id = id
    msg = EmailMessage()
    msg['Subject'] = 'Your account information'
    msg['From'] = "MEAapis@mea.or.th"
    msg['To'] = receiver
    msg.set_content(
        f'Dear {receiver_name},\n\nHere are your information.\n\nUsername: {receiver_name}\nUniqueID: {requested_id}\n\nPlease use your uniqueID for token request and information update.')
    # Send the email via our own SMTP server.
    with smtplib.SMTP(host='10.110.206.200', port=25) as s:
        s.send_message(msg)
