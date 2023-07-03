import smtplib
# soon create an automatic email sender
fro, to = 'dennisungureanu0@gmail.com', 'dennjsu.business@gmail.com'
message = 'Join our mailing service.'
#simple mail transfer protocol import smtplib

# email = input("Email:")
# send = input("What to send to the email mentioned.")
# maybe make a file, put 'send' in a file and send that to an email
# but we would have to have a email to send it from

with smtplib.SMTP('smtp.gmail.com', 587) as smtserver:
    smtserver.ehlo()
    smtserver.starttls()
    smtserver.ehlo()
    smtserver.login('dennisungureanu0@gmail.com','rjhsnasaykelprxw')
    for i in range(1):
        smtserver.sendmail(fro, to, message)
        #this sends the message to spam
        print(i)