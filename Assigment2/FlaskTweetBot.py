#import flask
from requests_oauthlib import OAuth1Session
import json
from flask import Flask, request, render_template, redirect, url_for
from Forms import CreateTweet, SearchForm, DeleteForm

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

@app.route("/")
@app.route("/home")
def hello():
	posts = []
	return render_template('home.html',posts=posts)


@app.route('/createTweet', methods=['GET', 'POST'])
def createTweet():
    form = CreateTweet()

    if form.validate_on_submit():
        tweet=form.tweet.data
        response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json={"text": f"{tweet}"},
    )
        return redirect(url_for('hello'))
    return render_template('create.html',title='create', form=form)

# This is incomplete
@app.route('/searchTweet', methods=['GET'])
def searchTweet():
    keyword = request.args.get('keyword')
    response = oauth.get(
        "https://api.twitter.com/2/tweets/search/recent?query="+keyword
        )
    print(response.json())
    #return render_template('search.html',posts=posts)
    return response.json()

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
            return redirect(url_for('hello'))
        except:
            return redirect(url_for('delete'))
    return render_template('delete.html',title='delete', form=form)

app.run(port=80)