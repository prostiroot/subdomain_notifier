import json
import os
# check if there are any files in new_subdomains
# if so, check file contents and send email
# delete file after sending email

# email config from file
with open('email_config.json') as email_config:
    data = json.load(email_config)
    FROM = data['from']
    pwd = data['password']
    TO = data['to']

SUBJECT = "New subdomain alert"
success = False
def send_email(user, pwd, recipient, subject, body):
	global success
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
		success = True
	except Exception as inst:
		print(inst)

domains_file = open('list_of_domains.txt')
new_subdomains = []
domains_w_new_sd = []
for line in domains_file:
	line = line.rstrip('\n')
	a = os.path.exists("new_subdomains/new_"+line+".txt")
	if a:
		domains_w_new_sd.append("new_"+line+".txt")
		new_subdomains.append("new subdomains for: " + line + ":\n")
		new_domains_file = open("new_subdomains/new_"+line+".txt")
		for n_line in new_domains_file:
			new_subdomains.append(n_line)
	else:
		print("no new subdomain files found for: " + line)

if(len(new_subdomains) > 0):
	#print(new_subdomains)
	EMAIL_TEXT = ("New subdomain(s): \n" + "".join(new_subdomains))
	send_email(FROM, pwd, TO, SUBJECT,EMAIL_TEXT)
	# delete new subdomain files from /new_subdomains after email was sent
	if (success):
		for domain in domains_w_new_sd:
			os.remove('new_subdomains/'+domain)
			print("deleted new_subdomains/" + domain)