#REVISE IMPORTED LIBRARIES -- USE YAHOO FINANCE, PANDAS AND NUMPY TO DO STOCK MOVEMENT CALCULATIONS
#THEN USE https://docs.alpaca.markets/docs/getting-started-with-trading-api TO MAKE TRADES BASED ON RESULTS


import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import alpaca_trade_api as tradeapi

APCA_API_KEY_ID = "PK22SI8A4ZQ8M1IK4MHR"
APCA_API_SECRET_KEY = "kNln0dUCh1MOUl934cmOQYgXeSFxfMBaCKrxXVcy"

def send_mail():
    #Environment
    os.environ['APCA_API_BASE_URL'] = "https://paper-api.alpaca.markets"

    #API Credentials
    api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, api_version='v2')
    account = api.get_account()

    #Informer email details
    sender_address = 'mooseautotrader@gmail.com'
    app_pass = 'amcxdhuyxnpgwtkf'
    receiver_address = 'benedict.tannous@gmail.com'

    #Setup MIME

    message = MIMEMultipart()
    message['From'] = 'Trading Bot'
    message['To'] = receiver_address
    message['Subject'] = "Today's Trade Results"  # The subject line

   
    try:
        #The body and the attachments for the mail
        message.attach(MIMEText("testing!", 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, app_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        done = 'Mail Sent'
    except Exception as e:
        done = f"Failed to send mail. Error: {str(e)}"

    return done

result = send_mail()
print(result)
