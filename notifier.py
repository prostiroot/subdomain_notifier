import json

# email config from file
with open('email_config.json') as email_config:
    data = json.load(email_config)
    FROM = data['from']
    pwd = data['password']
    TO = data['to']

SUBJECT = "New subdomain alert"

def send_email(user, pwd, recipient, subject, body):
	import smtplib
	# Prepare actual message
	message = """From: %s \nTo: %s \nSubject: %s \n\n%s""" % (FROM,TO,SUBJECT,EMAIL_TEXT)
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(FROM, pwd)
		server.sendmail(FROM, TO, message)
		server.close()
		print ('successfully sent the mail')
	except Exception as inst:
		print(inst)