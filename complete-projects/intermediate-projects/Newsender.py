import smtplib
# soon create an automatic email sender
d = 'dennisungureanu0@gmail.com'
db = 'dennjsu.business@gmail.com'


email =['Sc842506@gmail.com', 'lbnqvgmhnqvfbe@protonmail.com', ]
message = """
Cheers, people who have signed up, we have our first email issue!

Coming to you from a future CEO, this newsletter will be a collection of snippets of wisdom I’ve got in my head.

So a few weeks ago, I was watching Ali Abdaal’s videos. My eye caught on something he said, that “Everyone should start a email newsletter.”. After he stated some valid reasons, I said to myself, “Valid, maybe I’ll start one.” Then I just forgot about it in a few days. (2x a week reason). Everyone does this. They tell themselves later, but everyone will forget about it later if you leave the issue just like that. Change must be rooted in action. I had a slight want, to create a email newsletter, but I felt it was too much work. In reality, I will be sending my thoughts in an email maybe 1-2 times a week. If I allocate my time accordingly, this doesn’t even waste much time, and even has benefits for me if I continue. 

What I noticed the past few days is that my fear, which was not having enough time, is completely ignorant. I waste several hours a day, and I cannot spend an hour or so, every week to do something new? If we are afraid of doing something new, can we really change ourselves, change our destiny?

In life we go through many opportunities. We must learn when to say ‘yes’, and when to say ‘no’. As a general rule, If you’ve got enough time, you shouldn’t say no to a habit that you know will not endanger your future. We usually have enough time, we just just tend to make excuses. 

“Only those who will risk going too far can possibly find out how far one can go.” - T.S. Elliot. 

This newsletter will be sent around once a week, maybe more. Thank you for reading thus far, and if you have any questions, concerns, requests, criticism, please message them to dennjsu.business@gmail.com

-Dennis
"""



fro, to = db, None
to = 'Sc842506@gmail.com'
# to = 'lbnqvgmhnqvfbe@protonmail.com'
#to = None


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
    for i in range(1):
        smtserver.sendmail(fro, fro, "message")
        # this sends the message to spam
        print(i+1)  # status if sent.