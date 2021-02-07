import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def do_remind_call(phone_number):
  call = client.calls.create(
                          url='https://raw.githubusercontent.com/willyspinner/addictionator/master/remind_voice_call.xml',
                          to=phone_number,
                          from_='+15017122661'
                      )
    