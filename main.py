import subprocess

email_reader_allowing = input("I allow Hocari to filter all my emails to protect me from scams, phishing, etc... (Please type: Yes or No) ") 
print(email_reader_allowing)

check_token = email_reader_allowing.startswith("Y" or "y")


if check_token == False:
    subprocess.call(['python', 'imap_server_setup.py'])






    






