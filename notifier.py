import urllib2
import time
import emails
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def internet_on():
    try:
        # as of november the third, saime is throwing code 503 to let the user
        # know that the site is down
        urllib2.urlopen('https://tramites.saime.gob.ve', timeout=20)
        return True
    except Exception as err:
        return False


def send_emails():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(emails.sender_email, emails.sender_password)
    msg = MIMEMultipart()
    # the subject is setted just to add more context
    msg['Subject'] = "Saime status service"
    body = "Saime is active!"
    msg.attach(MIMEText(body, 'plain'))
    for e in emails.emails_list:
        server.sendmail(emails.sender_email, e, msg.as_string())
    server.quit()


timer = 30
while True:
    if(internet_on()):
        print("found url")
        timer = 1800  # half an hour
        send_emails()
    else:
        print("error finding the url")
        timer = 30  # 30 seconds
    time.sleep(timer)
