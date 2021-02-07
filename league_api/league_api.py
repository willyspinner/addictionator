import requests
import os

"""
Requests from riot games API about league matches. Must have RIOT_TOKEN environment variable set.
"""

class LeagueAPI:
	def __init__(self):
		self.headers = { 'X-Riot-Token': os.environ['RIOT_TOKEN']}
		self.domain = 'https://na1.api.riotgames.com'

	def create_base_request(self, endpoint, params=None):
		"""
		Input: 
			- endpoint: endpoint of API request
			- params: parameters to pass in GET request
		Returns a get request to Riot API with the specified endpoint and parameters
		"""

		if not endpoint.startswith('/'):
			endpoint = '/' + endpoint

		return requests.get(self.domain + endpoint, params=params, headers=self.headers)

	def get_encrypted_summoner_id(self, summoner_name):
		"""
		Input: 
			- summoner_name: user_id of league user
		Returns the encrypted id of the user
		"""

		res = self.create_base_request(f'/lol/summoner/v4/summoners/by-name/{summoner_name}')
		return res.json()['id']

	def get_active_game(self, summoner_name):
		"""
		Input:
			- encrpyted_summoner_id: encrypted id of the user
		Returns json of user status and whether they are in an active game
		"""
		
		encrypted_summoner_id = self.get_encrypted_summoner_id(summoner_name)
		res = self.create_base_request(f'/lol/spectator/v4/active-games/by-summoner/{encrypted_summoner_id}')
		return res.json()
