#! /usr/bin/python3

from flask import Flask, render_template
from flask import request
from spellchecker import SpellChecker
import json
import random
import requests
import dictionary

# dictionaryapi.com api key for thesaurus
apikey = "dba020ec-28cf-44cc-b5f0-b93f1bfcd6f9"

# Fix to allow subfolder locations on the reverse proxy
class ReverseProxied(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

# NOTE: This should be it's own class probably 

def checkspelling(word):
    spell = SpellChecker()
    misspelled = spell.unknown([word])

    for w in misspelled:
        return spell.candidates(w)

def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
               yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x

def get_synonyms(word):
    url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/%s?key=%s" % (word, apikey)
    response = requests.get(url).text
    json_data = json.loads(response)
    syns = list(findkeys(json_data, 'syns'))
    # Iterate and recurse your way to a list of synonym lists!
    synlists = [s for g in syns for s in g ]

    return synlists

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['word']

    wordlist = open('words.txt')
    line = next(wordlist)
    # Pick a random word from the word list file
    for num, line in enumerate(wordlist):
        if random.randrange(num + 2):
            continue
        word = line.rstrip("\n")
    wordlist.close()

    words = get_synonyms(word)
    defin = dictionary.get_defin(word)

    return render_template(
        'index.html', word=word, synonyms=words, definitions=defin)


@app.route('/words/<word>', methods=['GET', 'POST'])
def get_words(word):
    if request.method == 'POST':
        word = request.form['word']
    elif request.method == 'GET':
        word = word

    words = get_synonyms(word)
    defin = dictionary.get_defin(word)
    checkword = checkspelling(word)

    return render_template(
        'index.html', word=word, synonyms=words, definitions=defin, spellcheck=checkword)


# For easier web development
# Send no-cache headers to browser
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.config.update(TEMPLATES_AUTO_RELOAD=False)
    #app.config.update(TEMPLATES_AUTO_RELOAD=True)
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    #app.run(host='localhost', port=5000, threaded=True, debug=True)  
    app.run(host='localhost', port=5000, threaded=True, debug=False)