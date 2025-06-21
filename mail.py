import smtplib
from email.message import EmailMessage
import email.message


def email(person,cushion_width, span_of_cushion, no_of_layers, total_area, cost):
	
	
	email = person
	email_user = "fabrix360.com@gmail.com"
	email_send = email
	subject = f"fabrix360.com Your ETFE cost query skylight|facade" 
	# msg = MIMEMultipart()//no more needed becaus eyou imported sendemail instead i deleted MIMEM imports
	msg = EmailMessage()
	msg['from'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject

	# message = task+"  with remark status"+Remark
	
	body = f"""Dear user, thank you for reaching out!\n
	 For Panel width of {cushion_width} m \n
	 Panel span of {span_of_cushion} m \n
	 Panel number of layers {no_of_layers} no. \n
	 Subject to minimum total area of skylight/facade of {total_area} m2 \n

	  Cost/Price is AED  {cost}  per m2     (3.68 AED = 1 USD$)\n

	  This cost excludes supporting steel structures and any thing not related to ETFE. It also assumes standard print on ETFE-non colored- \n 
	  Note that this is not applicable on non straight forward rectangular cushions as shown in our webapp, for other special shapes and complexity feel free to reach us out on | www.fabrix360.com | management@fabrix360.com | \n

	  Disclaimer: Constructions costs are complicated and firm prices must be confirmed from specialists. \n 


	  We reamin at your disposal """
	msg.add_alternative(body)
	# text = msg.as_string()
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	
	# server.starttls() /because you used SMTP_SSL and changed port to 465
	server.login(email_user, 'mrzzbdfwsfzvtneh')
	# server.sendmail(email_user, email_send, text)
	server.send_message(msg)
	server.quit()
	emailme(person,cushion_width, span_of_cushion, no_of_layers, total_area, cost)

def emailme(person,cushion_width, span_of_cushion, no_of_layers, total_area, cost):
	email = 'management@fabrix360.com'
	email_user = "fabrix360.com@gmail.com"
	email_send = email
	subject = f"user in fabrixhub" 
	# msg = MIMEMultipart()//no more needed becaus eyou imported sendemail instead i deleted MIMEM imports
	msg = EmailMessage()
	msg['from'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject

	# message = task+"  with remark status"+Remark
	
	body = f"""{person} is reaching out!\n
	 For Panel width of {cushion_width} m \n
	 Panel span of {span_of_cushion} m \n
	 Panel number of layers {no_of_layers} no. \n
	 Subject to minimum total area of skylight/facade of {total_area} m2 \n

	  Cost/Price is AED  {cost}  per m2     (3.68 AED = 1 USD$)\n

	   \n 
	   """
	msg.add_alternative(body)
	# text = msg.as_string()
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	
	# server.starttls() /because you used SMTP_SSL and changed port to 465
	server.login(email_user, 'mrzzbdfwsfzvtneh')
	# server.sendmail(email_user, email_send, text)
	server.send_message(msg)
	server.quit()


def emailnote():
	email = 'management@fabrix360.com'
	email_user = "fabrix360.com@gmail.com"
	email_send = email
	subject = f"user in HOME" 
	# msg = MIMEMultipart()//no more needed becaus eyou imported sendemail instead i deleted MIMEM imports
	msg = EmailMessage()
	msg['from'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject

	# message = task+"  with remark status"+Remark
	
	body = f"""some one in home!\n
	 

	   \n 
	   """
	msg.add_alternative(body)
	# text = msg.as_string()
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	
	# server.starttls() /because you used SMTP_SSL and changed port to 465
	server.login(email_user, 'mrzzbdfwsfzvtneh')
	# server.sendmail(email_user, email_send, text)
	server.send_message(msg)
	server.quit()


# def email(useremail,message):
	
	
# 	email = "fabrix360.com@gmail.com"
# 	email_user = "fabrix360.com@gmail.com"
# 	email_send = email
# 	subject = f"Message from Heroku app by {useremail}"
# 	# msg = MIMEMultipart()//no more needed becaus eyou imported sendemail instead i deleted MIMEM imports
# 	msg = EmailMessage()
# 	msg['from'] = email_user
# 	msg['To'] = email_send
# 	msg['Subject'] = subject
# 	message = message
# 	body = message 
# 	msg.set_content(body)
# 	text = msg.as_string()
# 	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	
# 	# server.starttls() /because you used SMTP_SSL and changed port to 465
# 	server.login(email_user, 'jxmdkohbjmsuoxge')
# 	# server.sendmail(email_user, email_send, text)
# 	server.send_message(msg)
# 	server.quit()