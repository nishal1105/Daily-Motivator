from twilio.rest import Client
from config import account_sid,auth_token,phone_number

def twilio_conn_set (account_sid, auth_token):
  client = Client(account_sid, auth_token)
  return client

def send_whatsapp_text(client, quote):
  message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=quote,
      to= phone_number
      )
  return message.sid


client = twilio_conn_set(account_sid, auth_token)
