import random
import json
import urllib.parse
from user_agents import parse
import requests
from bs4 import BeautifulSoup
import sys

def select_user_agent():
	"""
	  return a random user agent from the list of valid user agents stored
	  in the resource directory.
	"""

	fh = open("resource/user-agents.txt", 'r')
	ignore_chars = ['#', ' ']
	agents = fh.readlines()
	agent_list = [] 
	user_agent = {}
	ua_parser_url = "http://www.useragentstring.com/?uas={%s}&getJSON=all"

	for agent in agents:
		if agent[0] in ignore_chars:
			continue
		else:
			agent_list.append(agent.strip())

	ua_string = random.choice (agent_list)
	ua_details = requests.get(ua_parser_url % ua_string)

	user_agent = {
		'user-agent': ua_string,
		'user-agent-encode': urllib.parse.quote(ua_string),
		'user-agent-details': ua_details.json()
	}

	return user_agent

def scrub_url(url):
	pass

def get_page(url):
	page = {}
	ua_dict = select_user_agent()

	headers = {'User-Agent': ua_dict["user-agent"]}
	r = requests.get(url, headers=headers)

	page['headers'] = headers
	page['soup'] = BeautifulSoup(r.text, 'html.parser')


	return page['soup']

if __name__ == "__main__":
	print(get_page("https://www.sitepoint.com/a-basic-html5-template/"))
