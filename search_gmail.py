import imaplib
import getpass

print "Google Username";
username = raw_input()
print "Google password";
password = getpass.getpass()

url = "imap.gmail.com"
email_account = imaplib.IMAP4_SSL(url)
email_account.login(username, password)
email_account.select('Inbox', readonly=True)
gmail_search='category:primary AND is:unread'
typ, data = email_account.search(None, 'X-GM-RAW', gmail_search)


for num in data[0].split():
    typ, data = email_account.fetch(num, '(BODY[HEADER.FIELDS (FROM TO SUBJECT)])')
    recip,send,subj = data[0][1].split("\r\n")[:3]
    print recip
    print send
    print subj
    print
email_account.close()
email_account.logout()
print "Done!"
