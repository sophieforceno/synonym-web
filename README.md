# Synonym-web
Self-hosted web-based thesaurus and dictionary written in Python 3.4.3.

Depends on thesaurus (https://github.com/Manwholikespie/thesaurus), PyDictionary, and flask

## Installation:
    git clone https://github.com/andyforceno/synonym-web.git
    cd synonym-web/
    pip install -r requirements.txt
    cd app/
    python3 app.py 
    Browse to http://localhost:5000

## Nginx Configuration:
    location / {
		proxy_pass         http://localhost:5000;
		proxy_redirect     off;
		proxy_set_header   X-Real-IP $remote_addr;
		proxy_set_header   X-Forwarded-Host $server_name;
		proxy_set_header   X-Forwarded-Proto $scheme;
			}

## Attribution:
Words.txt is a concatenation of word lists from: 
http://www.ashley-bovan.co.uk/words/partsofspeech.html

### Screenshot:

![alt text](https://raw.githubusercontent.com/andyforceno/synonym-web/master/synonym-web.jpg "Synonym-web on the desktop")

![alt text](https://raw.githubusercontent.com/andyforceno/synonym-web/master/mobile.jpg "Synonym-web on an Android phone")

