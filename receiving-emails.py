import datetime
x = datetime.datetime.now() - datetime.timedelta(1)                    #yesterday date
yesterday = x.strftime("%d")+"-"+x.strftime("%B")+"-"+x.strftime("%Y") #yesterday date, nicely formated

#SMTP --> sending emails (to server)
#IMAP (and pop3) --> receiving emails (from server)
#pop3 = move emails from server to client
#imap = copy emails from server to client

import imapclient
conn = imapclient.IMAPClient('imap.gmail.com' , ssl=True)
conn.login('nimaahmadvand28@gmail.com' , 'xskpizckmmcuhswv')
conn.select_folder('INBOX' , readonly=True)
#UIDs = conn.search(["SINCE "+yesterday])
#UIDs = conn.search(['NOT DELETED'])
UIDs = conn.search(['FROM', 'support@mega.nz'])
print (UIDs)
UID = input ("select one: ")
rawMessage = conn.fetch([UID] , ['BODY[]' , 'FLAGS'])

f = open('mail.html','w')
f.write(rawMessage)
f.close()
webbrowser.open_new_tab(str(mail.html))

#import pyzmail #easy_install pyzmail
#message = pyzmail.PyzMessage.factory(rawMessage[UID][b'BODY[]'])
#print (message#)