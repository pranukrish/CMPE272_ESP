#import flask
from re import A
from requests_oauthlib import OAuth1Session
import json
from flask import Flask, request, render_template, redirect, url_for
from Forms import CreateTweet, SearchForm, DeleteForm
import json


consumer_key = "M0cU10acS1mqtw4GGpwWaZhkI"
consumer_secret = "RaciSU6PbEqpkDxjtiIZWLPF2Y5cQqW79wD9tSBq8jk2w5FSSJ"
access_token = "1569020223587778560-HvtjB4OdGFFsJZtjwwIiuhnIaNppm8"
access_token_secret = "tR2L9nEhjXkZNrEr7tr7pkoFvDszU0r64O2RhMDgKnghr"

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

app = Flask(__name__)
app.secret_key = 'secret'

#posts = []

@app.route("/")
@app.route("/home/<a>")
def home(a=None):
    posts = []
    if a is None:
        return render_template('home.html', posts = posts, text = "Technovators Tweet Bot")
    elif a == "Successful":
        return render_template('home.html', posts = posts, text = "Tweet successful")
    elif a == "Deleted":
        return render_template('home.html', posts = posts, text = "Tweet deleted")

@app.route('/createTweet', methods=['GET', 'POST'])
def createTweet():
    form = CreateTweet()

    if form.validate_on_submit():
        tweet=form.tweet.data
        response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json={"text": f"{tweet}"},
    )
        return redirect(url_for('home', a='Successful'))
    return render_template('create.html',title='create', form=form, text="Tweet created")

# This is incomplete
@app.route('/searchTweet', methods=['GET', 'POST'])
def searchTweet():
    posts = []
    form = SearchForm()

    if form.validate_on_submit():
        userId = form.userId.data
    
        response = oauth.get(
        "https://api.twitter.com/2/tweets/search/recent?query="+userId
        )
        #print(response.json())
        
        #.stringify()
        posts = response.json()['data']
        #json.stringify(posts)
    return render_template('search.html',title='search', form=form, posts=posts)

@app.route('/deleteTweet', methods=['GET', 'POST'])
def deleteTweet():
    form = DeleteForm()
	
    if form.validate_on_submit():
        deleteTweetId=form.deleteTweetId.data
        try:
            #delt = api.destroy_status(deleteTweetId)
            response = oauth.delete(
        "https://api.twitter.com/2/tweets/{}".format(deleteTweetId)
        ) 
            return redirect(url_for('home', a='Deleted'))
        except:
            return redirect(url_for('delete'))
    return render_template('delete.html',title='delete', form=form )

app.run(port=80, debug=True)