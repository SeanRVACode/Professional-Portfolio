from flask import Flask,redirect,render_template,jsonify,request
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

@app.route('/search_brew',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        return render_template('search.html')

def get_brewery_list():
    #TODO worry about how I'm going to add multiple filters or not filter by something
    url = 'https://api.openbrewerydb.org/v1/breweries?by_city=richmond&by_state=virginia&per_page=100'
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
        key_new = re.sub(r'[_]+', ' ', key).strip().title()
        new_json_data[key_new] = value
    
    return new_json_data