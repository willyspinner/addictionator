import os
import urllib
from twilio.rest import Client

class TwilioAPI:
	def __init__(self):
		"""
		Your Account Sid and Auth Token from twilio.com/console
		and set the environment variables. See http://twil.io/secure
		"""

		self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
		self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
		self.twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
		self.client = Client(self.account_sid, self.auth_token)

		self.call_domain = 'http://twimlets.com/echo?Twiml='

	def do_remind_call(self, phone_number:str):
		"""
		see this: https://www.twilio.com/labs/twimlets/echo
		Input:
			- phone_number: phone number to send calls to
		Sends a phone call to phone_number with contents of remind_voice_call.xml
		"""

		with open('./remind_voice_call.xml') as f:
			remind_voice_call_xml = urllib.parse.quote_plus(f.read())
	
		call = self.client.calls.create(
			url = self.call_domain + remind_voice_call_xml,
			to = phone_number,
			from_ = self.twilio_phone_number
		)
		return call
		
	def do_remind_sms(self, phone_number:str):
		"""
		Input:
			- phone_number: phone number to send calls to
		Sends a SMS to phone_number with contents of sms_content.txt
		"""
		sms = self.client.messages.create(
				body=open('sms_content.txt', 'r').read(),
				to=phone_number,
				from_=self.twilio_phone_number
			)
		return sms