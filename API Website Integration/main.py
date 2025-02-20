from flask import Flask,redirect,render_template,jsonify
from flask_bootstrap import Bootstrap5
import requests
import json

app = Flask(__name__)
Bootstrap5(app)


@app.route('/brewery_lookup')
def home():
    
        
    data = get_single_brewery()
    print(data)
    return render_template('brewery_lookup.html',data=data)


def get_single_brewery():
    url = 'https://api.openbrewerydb.org/v1/breweries/random'
    print('Running Data')
    r = requests.get(url)
    json_data = r.json()
    return json_data

