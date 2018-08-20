#! /usr/bin/python3

from flask import current_app, Flask, render_template
from flask import redirect, request, session, url_for
import random
import synonyms
import dictionary

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    wordlist = open('words.txt')
    line = next(wordlist)
    # Pick a random word from the word list file
    for num, line in enumerate(wordlist):
      if random.randrange(num + 2): continue
      word = line.rstrip("\n")

    words = synonyms.get_synonyms(word)
    defin = dictionary.get_defin(word)

    return render_template('index.html', word=word, synonyms=words, definitions=defin)

@app.route('/word/<word>', methods=['GET', 'POST'])
def get_words(word):
    if request.method == 'POST':
        word = request.form['word']
    elif request.method == 'GET':
        word = word

    words = synonyms.get_synonyms(word)
    defin = dictionary.get_defin(word)

    return render_template('index.html', word=word, synonyms=words, definitions=defin)

if __name__ == '__main__':
    app.config.update(TEMPLATES_AUTO_RELOAD=True)
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    app.run(host='0.0.0.0', port=5000, threaded=True)