__author__ = 'spencer'
from flask import Flask, request, render_template
from chatbot.chatbot import init, generate_sentence

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello.'


@app.route('/b')
def bot():
    return render_template('base.html')


@app.route('/send', methods=['POST'])
def send():
    return generate_sentence(request.form['input_field'])

if __name__ == '__main__':
    init(None, None)
    app.run(debug=True)
