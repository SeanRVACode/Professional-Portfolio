from flask import Flask,redirect,render_template,jsonify
from flask_bootstrap import Bootstrap5
import requests
import json
import re

app = Flask(__name__)
Bootstrap5(app)


@app.route('/brewery_lookup')
def home():
    
        
    data = get_brewery_list()
    print(data)
    print('This is the data type beep boop', type(data[0]))
    # data_dict = proper_names(data)
    # print('These are the values',data_dict.values())
    headers_list = proper_names(data)
    return render_template('brewery_lookup.html',data=data,headers=headers_list)


def get_brewery_list():
    url = 'https://api.openbrewerydb.org/v1/breweries?per_page=10'
    print('Running Data')
    r = requests.get(url)
    print(r)
    json_data = r.json()
    
    # Convert to dict
    # brewery_dict = {brewery['id']: brewery for brewery in json_data}
    return json_data

def proper_names(json_data):
    json_data = json_data[0]
    # Create a new dictionary with modified keys
    new_json_data = {}
    for key, value in json_data.items():
        key_new = re.sub(r'[_\d]+', ' ', key).strip().title()
        new_json_data[key_new] = value
    
    return new_json_data