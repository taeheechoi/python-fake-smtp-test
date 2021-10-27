import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = '''From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
'''

if __name__ == '__main__':
  try:
    mail = smtplib.SMTP('127.0.0.1', 2525)
    mail.sendmail(sender, receivers, message)         
    print ('Successfully sent email')
  
  except:
    print ('Error: unable to send email')