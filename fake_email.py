import smtplib

from_email = 'from_email@test.com'
to_emails = ['to_email@test.com']

message = '''From: From Person <from_email@test.com>
To: To Person <to_email@test.com>
Subject: SMTP e-mail test

This is a fake e-mail message.
'''

if __name__ == '__main__':
  try:
    mail = smtplib.SMTP('127.0.0.1', 2525)
    mail.sendmail(from_email, to_emails, message)         
    print ('Successfully sent email')
  
  except:
    print ('Error: unable to send email')