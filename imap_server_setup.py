import email

user_email_imap_setup = input(str("Please enter your email address: "))

gmail_email_user_address_setup= user_email_imap_setup.endswith("gmail.com")
aol_email_user_address_setup= user_email_imap_setup.endswith("aol.com")
outlook_email_user_address_setup= user_email_imap_setup.endswith("outlook.com")
yahoo_email_user_address_setup= user_email_imap_setup.endswith("yahoo.com")
mail_email_user_address_setup= user_email_imap_setup.endswith("mail.com")

if gmail_email_user_address_setup == True:
        imap_server = "imap.gmail.com"
        print(user_email_imap_setup)
if aol_email_user_address_setup == True:
        imap_server = "imap.aol.com"
        print(user_email_imap_setup)
if outlook_email_user_address_setup == True:
        imap_server = "imap-mail.outlook.com"
        print(user_email_imap_setup)
if yahoo_email_user_address_setup == True:
        imap_server = "imap.mail.yahoo.com"
        print(user_email_imap_setup)
if mail_email_user_address_setup == True:
        imap_server = "imap.mail.com"
        print(user_email_imap_setup)
if user_email_imap_setup.endswith("hocari.com"):
        print("This address is not allowed. Please try again.")
        # Make it return to the beginning.

print(imap_server)
#else:
    #other_imap_server = input("Please enter your IMAP Server address: ")
    #print(other_imap_server)
