import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from threading import Thread  
from vars import *

class EmailSender():
    subject = "Log file"
    body = "PFA_THE_LOG_FILE"
    def send(self,fromaddr,toaddr,filename,sentfile='log.txt',password=None,smtp_server = 'smtp.gmail.com',smtp_port=587):
        # instance of MIMEMultipart
        msg = MIMEMultipart()
        # storing the senders email address  
        msg['From'] = fromaddr
        # storing the receivers email address 
        msg['To'] = toaddr
        # storing the subject 
        msg['Subject'] = self.subject
        #body of the mail
        body = self.body
        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        # open the file to be sent 
        attachment = open(filename, "rb")
        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form
        p.set_payload((attachment).read())
        # encode into base64
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % sentfile)
        # attach the instance 'p' to instance 'msg'
        msg.attach(p)
        # creates SMTP session
        #s = smtplib.SMTP('smtp.gmail.com', 587) #for Gmail
        s = smtplib.SMTP(smtp_server, smtp_port)
        # start TLS for security
        s.starttls()
        if password == None:
            password = getpass(prompt="Password= ")
        # Authentication
        s.login(fromaddr,password)
        # Converts the Multipart msg into a string
        text = msg.as_string()
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
        # terminating the session
        s.quit()
    def run(self,fromaddr,toaddr,filename,sentfile='logs.txt',password=None,smtp_server = 'smtp.gmail.com',smtp_port=587):
        self.send(fromaddr,toaddr,filename,sentfile=sentfile,password=password,smtp_server = smtp_server,smtp_port=smtp_port)

Sender = EmailSender() #global object
#Modify Subject using Sender.subject = "new subject title"
#Modify Body using Sender.body = "new body title"

def send(fromaddr,toaddr,filename,sentfile='logs.txt',password=None,smtp_server = 'smtp.gmail.com',smtp_port=587):
    global Sender
    Sender.run(fromaddr,toaddr,filename,sentfile=sentfile,password=password,smtp_server = smtp_server,smtp_port=smtp_port)

