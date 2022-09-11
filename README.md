# Synonym-web
Self-hosted web-based thesaurus and dictionary written in Python 3. I write fiction in my free time.
I wanted an easy-to-access, and ad-free, thesaurus, and so synonym-web was born. 

With Synonym-web you can: query for words in your browser, get synonyms, rhymes, defintions, etymology,
click on synonyms to see synonyms of those words, and offers spelling suggestions for mispelled words

Depends on pyspellchecker (https://github.com/barrust/pyspellchecker), Flask, Requests, and CherryPy (see requirements.txt)

Requires free API keys from dictionaryapi.com (https://www.dictionaryapi.com) for thesaurus and dictionary

## Installation:
	Sign up for API keys at dictionaryapi.com 
	git clone https://github.com/sophieforceno/synonym-web.git
    	cd synonym-web/
	Insert API keys in the `_key` variables in app.py	
	(Setting up a virtual environment is a good idea, but not covered here)
    	pip install -r requirements.txt
    	cd app/ 
	python3 wsgi.py
    	Browse to http://localhost:5000

## Nginx Configuration:
    location / {
		proxy_pass			http://localhost:5000;
		proxy_redirect		off;
		proxy_set_header	X-Real-IP $remote_addr;
		proxy_set_header	X-Forwarded-Host $server_name;
		proxy_set_header	X-Forwarded-Proto $scheme;
		proxy_set_header    Host $host;                                                                               
		proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;                                               
		proxy_set_header    X-Scheme $scheme;                                                                         
		proxy_set_header    X-Script-Name /;
			}

### Desktop:
![alt text](https://raw.githubusercontent.com/sophieforceno/synonym-web/master/synonymweb-ui-desktop.png "Synonym-web on the desktop")

### Mobile:
<img src="https://raw.githubusercontent.com/sophieforceno/synonym-web/master/synonymweb-ui-mobile.jpg" title="Syonynm-web on a mobile phone" height="600" width="387"></img>

## Attribution:
Words.txt is a concatenation of word lists from: 
http://www.ashley-bovan.co.uk/words/partsofspeech.html
