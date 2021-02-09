from database import UserDB
from league_api import LeagueAPI
from twilio_api import TwilioAPI

def run_addictionator():
    pass
    

if __name__ == "__main__":

    user_data = {
        "summoner_name": 'hashbrown32',
        "phone_number": '999-999-9999',
        "phone_call_choice": False,
        "text_message_choice": True,
    }

    db = UserDB("database/user_database.db")
    league_api = LeagueAPI()
    twilio_api = TwilioAPI()
    
    db.add_user(user_data)
    results = db.fetch_all_data()

    for summoner in results:
        if league_api.check_active(summoner.get("summoner_name")):
            if summoner.get("phone_call_choice"):
                twilio_api.do_remind_call(summoner.get("phone_number"))
                print(f'sending phone call to {summoner.get("summoner_name")}')
            if summoner.get("text_message_choice"): 
                twilio_api.do_remind_sms(summoner.get("phone_number"))
                print(f'sending text to {summoner.get("summoner_name")}')
        else:
            print(f'Summoner {summoner.get("summoner_name")} is not active right now')


    
