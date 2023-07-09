import smtplib
# soon create an automatic email sender
d = 'dennisungureanu0@gmail.com'
db = 'dennjsu.business@gmail.com'

fro, to = d, 'arinaelisau@gmail.com'
message = """
CHECK YOUR EMAIL"""

dju ='pbtmwsglirbshydi'
bju_pass = 'qczqtuyctdckbakb'
#simple mail transfer protocol import smtplib

# email = input("Email:")
# send = input("What to send to the email mentioned.")
# maybe make a file, put 'send' in a file and send that to an email
# but we would have to have a email to send it from

with smtplib.SMTP('smtp.gmail.com', 587) as smtserver:
    smtserver.ehlo()
    smtserver.starttls()
    smtserver.ehlo()
    #smtserver.login('dennisungureanu0@gmail.com','rjhsnasaykelprxw')
    smtserver.login(db, bju_pass)
    for i in range(25):
        smtserver.sendmail(fro, to, message)
        #this sends the message to spam
        print(i)