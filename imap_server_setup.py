import imaplib
from main import email_reader_allowing

check_token = email_reader_allowing.startswith("Y" or "y")

if check_token == False:
    print(True)

if check_token == True:
    exit()


user_email_imap_setup_test = "YOUR_EMAIL"
user_imap_setup_test = "YOUR_IMAP"

user_email_imap_setup = input("Please enter your email address: ")
gmail_email_user_address_setup= user_email_imap_setup.endswith("gmail.com")
aol_email_user_address_setup= user_email_imap_setup.endswith("aol.com")
outlook_email_user_address_setup= user_email_imap_setup.endswith("outlook.com")
yahoo_email_user_address_setup= user_email_imap_setup.endswith("yahoo.com")
mail_email_user_address_setup= user_email_imap_setup.endswith("mail.com")

if gmail_email_user_address_setup == True:
        # Need special requirement with third party app authorization bla bla
        imap_server = imaplib.IMAP4_SSL("imap.gmail.com")
        print("Your email is from gmail.com")
if aol_email_user_address_setup == True:
        imap_server = imaplib.IMAP4_SSL("imap.aol.com")
        print("Your email is from aol.com")
if outlook_email_user_address_setup == True:
        imap_server = imaplib.IMAP4_SSL("imap-mail.outlook.com")
        print("Your email is from outlook.com")
if yahoo_email_user_address_setup == True:
        imap_server = imaplib.IMAP4_SSL("imap.mail.yahoo.com")
        print("Your email is from yahoo.com")
if mail_email_user_address_setup == True:
        imap_server = imaplib.IMAP4_SSL("imap.mail.com")
        print("Your email is from mail.com")
if user_email_imap_setup.endswith("hocari.com"):
        print("This address is not allowed. Please try again.")
        # Make it return to the beginning.

print(imap_server)
#else:
    #other_imap_server = input("Please enter your IMAP Server address: ")
    #print(other_imap_server)



