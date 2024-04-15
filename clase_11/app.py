import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "David",
        "lastname": "Rangel",
        "socialMedia":
        [
            {"facebookUser": "dr1602"},
            {"instagramUser": "dr1602"},
            {"xUser": "dr1602"},
            {"linkedin": "dr-1602"},
            {"githubUser": "dr1602"}
        ],
        "blog": "https://ihealth.com",
        "author": "Miranda Espinoza"
    }
    return json.dumps(value)