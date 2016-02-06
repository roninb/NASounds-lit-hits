from flask import Flask
from flask import render_template

import os

import requests
import json

import soundcloud

app = Flask(__name__)
api_key = "X5YrFuP5L7iwOrmQB9Xx9ggrlMlVq42s6Ew5LXCn"
client = soundcloud.Client(client_id='f8902e59eb210853156eacc39a818ce9')
track = client.get('/tracks/181835738')
stream_url = client.get(track.stream_url, allow_redirects=False)

print stream_url.location

@app.route("/")
def home():
    url = "https://api.nasa.gov/planetary/sounds?limit=27&api_key=X5YrFuP5L7iwOrmQB9Xx9ggrlMlVq42s6Ew5LXCn"
    r = requests.get(url)
    j = json.loads(r.text)
    return render_template("index.html", sounds=j["results"])

@app.route("/rockets")
def rocks():
    url = "https://api.nasa.gov/planetary/sounds?q=rockets&limit=5&api_key=X5YrFuP5L7iwOrmQB9Xx9ggrlMlVq42s6Ew5LXCn"
    r = requests.get(url)
    j = json.loads(r.text)
    print j["results"]
    return render_template("index.html", sounds=j["results"])

if __name__ == '__main__':
    app.secret_key = 'hackfsu'
    app.run(debug=True)
