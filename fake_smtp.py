import argparse
import asyncore
import smtpd
from datetime import datetime
from pathlib import Path


def get_date_time_stamp():
    today = datetime.now()
    timestamp = str(today.timestamp()).split('.')[0]
    return f'{today:%m_%d_%Y}_{timestamp}' # 10_26_2021_1635302925

class FakeSMTPServer(smtpd.SMTPServer):
    def __init__(*args, **kwargs):
        smtpd.SMTPServer.__init__(*args, **kwargs)
        print ('Running fake smtp server')

    def process_message(*args, **kwargs):

        destination = Path.cwd() / f'mail/{get_date_time_stamp()}.eml'
        
        with open (destination, 'w') as file:
            # file.writelines(f'{arg}\n' for arg in args) # all args. 
            file.writelines(str(args[4]).replace('\\n', '\n')) # email content only and replace \n to newline

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', type=str, default='127.0.0.1', help='server to listen on. Default 127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=2525, help='port to listen on. Default 2525.')
    args = parser.parse_args()
    # python fake_smtp.py -s 1.1.1.1 -p 2525
    
    smtp_server = FakeSMTPServer((args.server, args.port), None)
    
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        smtp_server.close()
