# Bulk send Emails to anyone (Especially recruiters)

## Run the following commands to get started

Install all libraries
`pip install -r requirements.txt`

Create an app password for your gmail account by following [this blog](https://www.letscodemore.com/blog/smtplib-smtpauthenticationerror-username-and-password-not-accepted/)

Once you've generated the app password
- Create a .env file in the root directory
- create a key value pair `APP_PASSWORD=<app_password_generated_in_previous_step>`

- Update excel data with list of your favourite companies
- Create a template and run the main.py file

Use the htmlMail.py file if you want to create more complext layouts using HTML

