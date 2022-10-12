import smtplib

sender_email = 'YOUR_EMAIL'
sender_password = 'YOUR_EMAIL_PASSWORD'

sent_from = sender_email
to = ['RECIEVER_EMAIL']
subject = 'TYPE YOUR OWN SUBJECT'
# Next line doesn't accept accents!
body = 'Voici un email envoye automatiquement (enfin quand tout sera termine) par Python, pour Safe Anywhere.'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('YOUR_IMAP', 465)
    smtp_server.ehlo()
    smtp_server.login(sender_email, sender_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
