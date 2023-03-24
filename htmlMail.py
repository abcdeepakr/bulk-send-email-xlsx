import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
from dotenv import load_dotenv

# Load env file
load_dotenv()

# Access env variables
app_password = os.getenv('APP_PASSWORD')

# Create the message
message = MIMEMultipart()
message['From'] = 'Youremail@gmail.com'
message['To'] = 'recepientEmail@xyz.com'
message['Subject'] = 'Test email with link'

# Create the HTML body with a link
html = """\
<html>
  <body>
        <a href="#"> Write HTML Here </a>
        <ul>
            <li>Create templates</li>
            <li>Send bulk emails</li>
            <li>df FTW</li>
        </ul>
        <i><b>
        Best, <br>
        Name
        </b></i>
    </body>
</html>
"""

# Attach the HTML body to the message
body = MIMEText(html, 'html')
message.attach(body)

# Send the message using SMTP
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('yourEmail@gmail.com', app_password)
    server.sendmail('yourEmail@gmail.com', 'recepientEmail@xyz.com', message.as_string())

print("email sent")