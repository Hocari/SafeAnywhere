import imaplib
import pprint

imap_host = 'mail.privateemail.com'
imap_user = 'contact@hocari.com'
imap_pass = 'Oddpaste90'

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

a, b = imap.search(None, '(UNSEEN)')

if b[0]:
        c = b[0]
        d = c.split()
        e = d[-1]

        data = imap.fetch(e,'(BODY[1.1] BODY[HEADER.FIELDS (SUBJECT FROM)])')

        body_data = data[1][0][1]
        header_data = data[1][1][1]
        print(body_data) #Now "body_data" always contains the body, i.e. only the "text/plain" section
