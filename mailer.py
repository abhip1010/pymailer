

from threading import Timer,Thread,Event
from datetime import datetime

    # Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
import email
from email.mime.base import *
from email.mime.multipart import *
from email.mime.text import *

def send_mail(
              subject,
              body,
              recipient,
              author='abhi.p1010@gmail.com',
              author_name='Abhishek',
              recipient_name='Abhi'):
    # Create the message
    msg = MIMEText(body)
    msg['To'] = email.utils.formataddr((recipient_name, recipient))
    msg['From'] = email.utils.formataddr((author_name, author))
    msg['Subject'] = subject

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    # server.set_debuglevel(True) # show communication with the server
    server.starttls()
    server.login('abhi.p1010@gmail.com', 'Tsuguru0')
    try:
        server.sendmail(author, [recipient], msg.as_string())
    finally:
        server.quit()



class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def send_the_regular_mail(self):
        print('abotu to send emails')
        send_mail('Email from mailer',
                'content created at {}'.format(datetime.now()),
                'abhi.pandey@gmail.com')
        print('Mail Sent')
    def run(self):
        self.send_the_regular_mail()
        while not self.stopped.wait(50):
            self.send_the_regular_mail()
            # call a function



stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()
# this will stop the timer


# stopFlag.set()

