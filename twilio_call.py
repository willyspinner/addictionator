import os
import urllib
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
client = Client(account_sid, auth_token)

def do_remind_call(phone_number):
  # see this: https://www.twilio.com/labs/twimlets/echo
  with open('./remind_voice_call.xml') as f:
    remind_voice_call_xml = urllib.parse.quote_plus(f.read())
  
  call = client.calls.create(
                          url=f'http://twimlets.com/echo?Twiml={remind_voice_call_xml}',
                          to=phone_number,
                          from_=twilio_phone_number
                      )
    
