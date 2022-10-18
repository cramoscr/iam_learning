# send_email.py
# -------------
# Updated: cramos 27/set/2022
# [ Based on TheLondonApp 100DaysOfPython course ]
# Notes:
#    a. Uses smptlib for sending basic email from Gmail account to Yahoo
#    b. smtplib is included by default on Python
#    c. Gmail mailbox will require to generate an "App password" for access

import smtplib

# Google App Password:
#    email: securesally@gmail.com
# password: xvotyziuastvcofn

my_email = "cramos.dev.test@gmail.com"
#my_password = "NOn$ecur3_At_@11"
my_password = "xvotyziuastvcofn"

# Possible SMTP servers:
#      Gmail: smtp.gmail.com
#    Hotmail: smtp.live.com
#    Outlook: outlook.office365.com
#      Yahoo: smtp.mail.yahoo.com

with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()
	logged_in = False

	try:
		connection.login(user=my_email, password=my_password)
		logged_in = True
	except smtplib.SMTPAuthenticationError as serr:
		print('Errores:', serr)

	if logged_in:
		try:
			connection.sendmail(
    			from_addr=my_email,
    			to_addrs="cramoscr@yahoo.com",
    			msg="Subject: Hi again...\n\n This is the body of the email.")
		except Exception as Ex:
			print('No se pudo enviar correo', Ex)


