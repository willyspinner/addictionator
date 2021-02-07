import requests
import os

"""
Requests from riot games API about league matches. Must have RIOT_TOKEN environment variable set.

"""

def create_base_request(endpoint, params=None):
  headers={ 'X-Riot-Token': os.environ['RIOT_TOKEN']}
  if not endpoint.startswith('/'):
    endpoint = '/' + endpoint
  return requests.get(f'https://na1.api.riotgames.com{endpoint}', params=params, headers=headers)

def get_encrypted_summoner_id(summoner_name):
  res = create_base_request(f'/lol/summoner/v4/summoners/by-name/{summoner_name}')
  return res.json()['id']

def get_active_game(encrypted_summoner_id):
  res = create_base_request(f'/lol/spectator/v4/active-games/by-summoner/{encrypted_summoner_id}')
  return res.json()
