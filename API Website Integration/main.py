from flask import Flask,redirect,render_template,jsonify
from flask_bootstrap import Bootstrap5
import requests
import json
import re

app = Flask(__name__)
Bootstrap5(app)


@app.route('/brewery_lookup')
def home():
    
        
    data = get_single_brewery()
    data_edited = proper_names(data)
    print(data_edited)
    
    return render_template('brewery_lookup.html',data=data_edited)


def get_single_brewery():
    url = 'https://api.openbrewerydb.org/v1/breweries/random'
    print('Running Data')
    r = requests.get(url)
    json_data = r.json()
    return json_data

def proper_names(json_data):
    json_data = json_data[0]
    # Create a new dictionary with modified keys
    new_json_data = {}
    for key, value in json_data.items():
        key_new = re.sub(r'[_\d]+', ' ', key).strip().title()
        new_json_data[key_new] = value
    
    return new_json_data