import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import smtplib

prev_input = 0
#data = time.strftime("%H:%M:%S")
#data_s = time.strftime("%c")
#data_f = time.strftime("%c")
while True:
  input = GPIO.input(4)
  if ((prev_input) != input):
    if (input==0):
        #create email
                message = """PREZENTA TENSIUNE - PARC ULMU  """ + time.strftime("%c")
                msg = MIMEText(message)
                msg['subject'] = 'Alerta HUPA ULMU - Stop'
                msg['from'] = 'hupa@mondoit.ro'
                msg['to'] = 'recipient@mondoit.ro'
                # send mail
                #s = smtplib.SMTP('smtp.mailgun.org:25')
                s = smtplib.SMTP('smtp.mailgun.org',587)
                s.login('user_login@domeniu.ro' , 'parola')
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit
                print ("Alerta STOP")
                time.sleep(5)
    else:
        #create email
                message = """LIPSA TENSIUNE - PARC ULMU """ + time.strftime("%c")
                msg = MIMEText(message)
                msg['subject'] = 'Alerta HUPA ULMU - Start'
                msg['from'] = 'hupa@mondoit.ro'
                msg['to'] = 'recipient@mondoit.ro'
                # send mail
                #s = smtplib.SMTP('smtp.mailgun.org:25')
                s = smtplib.SMTP('smtp.mailgun.org',587)
                s.login('user_login@domeniu.ro' , 'parola')
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit
                print ("Alerta START")
                time.sleep(5)
    prev_input = input
    #slight pause to debounce
    time.sleep(0.05)
