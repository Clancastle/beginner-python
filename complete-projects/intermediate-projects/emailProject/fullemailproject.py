"""this is just the script to send the email. i can host it to the
cloud and have it run every 5 days/bi-weekly. put email in input, sends auto, if no input
no send.
"""

#open file of emails, do the dodo
import smtplib

user = 'dennjsu.business@gmail.com'
password = 'qczqtuyctdckbakb'
emails = ["dennisungureanu0@gmail.com", user, 'Sc842506@gmail.com', 'lbnqvgmhnqvfbe@protonmail.com',
          'andrewli3645@gmail.com']
emails = [user, "apple@gmail.com", 'apple1@gmail.com']
# email = [email for email in emails] #can place list as a (to send) and it will work

msg = """
"""

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # identifies with mail server
    smtp.starttls()  # encrypts traffic (email)
    smtp.ehlo()  # re-identifies with mail server

    smtp.login(user, password)

    smtp.sendmail(user, emails, None)

"""Plan:
make a decent webpage w js and html, css, and connect to my backend, 
here, which should make 'emails' a list, open in a document, (learn to save the data)
then i send the emails signing up (before w rgex) here to emails. """
