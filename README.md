# Synonym-web
Self-hosted web-based thesaurus and dictionary written in Python 3.4.3. I write fiction in my free time. 
I wanted an easy-to-access and ad-free thesaurus, and so synonym-web was born.

Depends on thesaurus (https://github.com/Manwholikespie/thesaurus), PyDictionary, flask, and CherryPy (see requirements.txt)

Update: I will be adding spellchecking for search queries using https://github.com/barrust/pyspellchecker as my biggest issue in my personal use has been misspelling, and then having to search the web for the correct spelling, and then enter that into synonym-web.

## Installation:
    git clone https://github.com/andyforceno/synonym-web.git
    cd synonym-web/
    (Setting up a virtual environment is probably a good idea, not covered here)
    pip install -r requirements.txt
    cd app/ 
	python3 wsgi.py
    Browse to http://localhost:5000

## Nginx Configuration:
    location / {
		proxy_pass         http://localhost:5000;
		proxy_redirect     off;
		proxy_set_header   X-Real-IP $remote_addr;
		proxy_set_header   X-Forwarded-Host $server_name;
		proxy_set_header   X-Forwarded-Proto $scheme;
			}

### Desktop:
![alt text](https://raw.githubusercontent.com/andyforceno/synonym-web/master/synonym-web.jpg "Synonym-web on the desktop")

### Mobile:
<img src="https://raw.githubusercontent.com/andyforceno/synonym-web/master/mobile.jpg" title="Syonynm-web on a mobile phone" height="600" width="387"></img>

## Attribution:
Words.txt is a concatenation of word lists from: 
http://www.ashley-bovan.co.uk/words/partsofspeech.html
