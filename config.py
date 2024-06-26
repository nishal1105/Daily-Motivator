import os
import secrets

account_sid = os.environ.get('TWILIO_ACC_ID')
auth_token = os.environ.get('TWILIO_ACC_TOKEN')
phone_number = os.environ.get('PHONE')