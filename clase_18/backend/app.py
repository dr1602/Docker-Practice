from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "David",
        "lastname": "RS",
        "socialMedia":
        {
            "facebookUser": "drs1602",
            "instagramUser": "drs1602",
            "xUser": "drs1602",
            "linkedin": "drs'1602",
            "githubUser": "drs1602"
        },
        "blog": "https://ihealth.com",
        "author": "Miranda Espinoza"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)