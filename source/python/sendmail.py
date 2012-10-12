import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(send_from, send_to, subject, text, files=[]):
    assert type(send_to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    # perhaps reconfigure it to send from beijing3ds.org server
    smtp = smtplib.SMTP('smtp.gmail.com', 587) #port 465 or 587
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('beijing3ds@gmail.com','beijing3DAYSTARTUP')

    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


"""
usage:

import sendmail
sendmail.send_mail('beijing3ds@gmail.com', ['apply@beijing3ds.org'], 'email subject', 'email body text', ['attachment1', 'attachment2'])
"""
