__author__ = 'spencer'

import argparse
from chatbot import init, generate_sentence
from flask import Flask, request, render_template, session, redirect
import tweepy

app = Flask(__name__)
CONSUMER_KEY = None
CONSUMER_KEY_SECRET = None
API = None

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/oauth/twitter')
def oauth_twitter():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET, 'http://127.0.0.1:5000/oauth/twitter/callback')
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print('Error! Failed to get request token.')

    session['request_token'] = (auth.request_token.copy())

    return redirect(redirect_url)


@app.route('/oauth/twitter/callback')
def oauth_twitter_callback():
    global API

    confirmation = request.args.get('oauth_verifier')
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.request_token = session['request_token']
    try:
        auth.get_access_token(confirmation)
    except tweepy.TweepError:
        print('Error! Failed to get access token.')

    API = tweepy.API(auth)
    return redirect('/b/{}'.format(API.me().screen_name))


@app.route('/b/<uname>')
def bot(uname):
    init(API, [uname])
    return render_template('base.html')


@app.route('/send', methods=['POST'])
def send():
    return generate_sentence(request.form['input_field'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flask-powered twitterbrains!')
    parser.add_argument('ck', metavar='consumer_key', help='OAuth consumer key')
    parser.add_argument('cks', metavar='consumer_key_secret', help='OAuth consumer key secret')
    parser.add_argument('fas', metavar='flask_app_secret', help='Flask application secret')
    args = parser.parse_args()

    CONSUMER_KEY = args.ck
    CONSUMER_KEY_SECRET = args.cks
    app.secret_key = args.fas

    app.run(host='0.0.0.0', debug=False)
