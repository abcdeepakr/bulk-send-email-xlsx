import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
from dotenv import load_dotenv
import pandas as pd

# Load env file
load_dotenv()

# Access env variables
'''
To get the app password for gmail users
visit https://myaccount.google.com/security?hl=en
make sure 2FA is turned on
search for App passwords in the search box above
create an app password
store it in .env

read this blog for more clarity => https://www.letscodemore.com/blog/smtplib-smtpauthenticationerror-username-and-password-not-accepted/
'''
app_password = os.getenv('APP_PASSWORD')

# Use the variables in your script
# ...

# Define email content

df = pd.read_excel('./companies.xlsx',sheet_name=0)

for index, row in df.iterrows():
    sender = 'yourEmail@gmail.com'
    receiver = row['email']
    subject = f"{row['position']} at {row['company name']}"


    body = f"""
    hello {row['recruiter_name']} i am deepak
    i want to apply for position of {row['position']} at you company {row['company name']}
    i want to work with you guys
    use chatgpt change this text
    """

    email_text = f"""\
    From: {sender}
    To: {receiver}
    Subject: {subject}

    {body}
    """

    # Log in to your Gmail account
    smtp_server = 'smtp.gmail.com'
    port = 587  # For starttls
    password = app_password
    context = smtplib.SMTP(smtp_server, port)
    context.starttls()
    context.login(sender, password)

    # Send the email
    context.sendmail(sender, receiver, email_text)

    # Close the connection
    context.quit()

    print(f'Email sent successfully to {row["company name"]} !')





