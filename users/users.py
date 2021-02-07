from league_api import LeagueAPI
from twilio_api import TwilioAPI

"""
We want to eventually convert this to a database instead of class which stores
summoner name, phone number, whether they want to receive phone call and whether
they want to receive text message
"""

class User:
    def __init__(self, summoner_name:str, phone_number:str, phone_call:bool=False, text_msg:bool=False):
        self.summoner_name = summoner_name
        self.phone_number = phone_number
        self.phone_call = phone_call
        self.text_msg = text_msg

        self.league_api = LeagueAPI()
        self.twilio_api = TwilioAPI()

    def check_active(self):
        res = self.league_api.get_active_game(self.summoner_name)
        if res['status']['status_code'] == 404:
            return False
        return True

    def send_phone_call(self):
        pass

    def send_text_message(self):
        pass

    def send_notification(self):
        if self.phone_call:
            self.send_phone_call()
        if self.text_msg:
            self.send_text_message()