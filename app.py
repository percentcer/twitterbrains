__author__ = 'spencer'
from flask import Flask, request, render_template
from chatbot.chatbot import init, authenticate_twitter, generate_sentence

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello.'


@app.route('/b/<uname>')
def bot(uname):
    init(None, [uname])
    return render_template('base.html')


@app.route('/send', methods=['POST'])
def send():
    return generate_sentence(request.form['input_field'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
