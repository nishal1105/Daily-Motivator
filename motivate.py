import requests
from twilio_conn import client, send_whatsapp_text

##############################################
##############################################

############### Author: Nishal ###############
## Gets Quote of the day from ZENQUOTES API ##
######### Sends the Code to whatsapp #########

##############################################
##############################################


def qodPyMotiv():
    res = requests.get(url = "https://zenquotes.io/api/quotes")
    data = res.json()[0]
    
    status = res.status_code
    match status:
        case 200:
            quote = data ['q'] + '\n -' + data ['a']
        case 400:
            quote = data ['error'] ['message']
        case _:
            quote = "No Response"
    return quote

quote = qodPyMotiv()
print (quote)
