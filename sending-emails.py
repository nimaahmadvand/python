import smtplib
conn = smtplib.SMTP('smtp.gmail.com' , 587)
conn.ehlo()
conn.starttls()
conn.login('nimaahmadvand28@gmail.com' , 'xskpizckmmcuhswv') #login to smtp.gmail.com with your account.
                                                             #use https://myaccount.google.com/apppasswords
                                                             #to generate an application specific password.

#------sending an email------
conn.sendmail('nima@mylab.local' , 'nimaahmadvand77@yahoo.com' , 'Subject: this is a test from python\n\nDear Nima,\nSo long, and thanks for all the fish.')
conn.quit()
