"""
	get a url
	scan url and pull out key information by section
		- response
			* error
			* http response
		- meta
			* title
			* keywords
		- headers (h1...h6)
		- paragraphs
		- links
			* text
			* destination
		- scan details
			- date/time
			- url
	store results in dictionary
"""

from bs4 import BeautifulSoup as bs
import requests
import os, sys
from util import select_user_agent
from datetime import datetime as dt
import json

url = sys.argv[1]
# TODO: add in validation for URL

ua = select_user_agent()['user-agent']

# initialise the page scan with details of setup
page = {
	'url': url,
	'scan-stats': {
		'scan-ua': ua,
		'scan-time': dt.now().strftime("%Y-%m-%d:%H:%M:%S")
	}
}

r = requests.get(url, headers={ 'user-agent': ua}, timeout=1.00)
h = r.headers	

# TODO: add in redirect detection / handling
# TODO: add in cookie handling (GDPR)

# populate header information for scan
page["response"] = r.status_code,
page["headers"] = {
	'content-type': h['content-type'],
	#'last-modified': h['last-modified'],
	'set-cookie': h['set-cookie'],
	#'gdpr': h['x-gdpr']
}
page["content"] = {
	'raw': r.text
}



if __name__ == "__main__":
	print (json.dumps(page, indent=2))