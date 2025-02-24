from flask import Flask,redirect,render_template,jsonify,request,url_for
from flask_bootstrap import Bootstrap5
import requests
import json
import re
from urllib.parse import urlencode

app = Flask(__name__)
Bootstrap5(app)

DEFAULT_URL = 'https://api.openbrewerydb.org/v1/breweries'

@app.route('/brewery_lookup')
def home():
    data = get_brewery_list()
    headers_list = proper_names(data)
    return render_template('brewery_lookup.html', data=data, headers=headers_list)

@app.route('/search_brew', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        params = {}
        b_name = request.form.get('brewName')
        b_city = request.form.get('cityName')
        if b_name:
            params['by_name'] = b_name
        if b_city:
            params['by_city'] = b_city

        query_string = urlencode(params)
        url = f"{DEFAULT_URL}?{query_string}"
        r = requests.get(url)
        json_data = r.json()
        create_map_link(json_data)
        headers_list = proper_names(json_data)
        
        return render_template('brewery_lookup.html', data=json_data, headers=headers_list)
    return render_template('search.html')

def get_brewery_list():
    #TODO worry about how I'm going to add multiple filters or not filter by something
    url = 'https://api.openbrewerydb.org/v1/breweries?&per_page=10'
    print('Running Data')
    r = requests.get(url)
    print(r)
    json_data = r.json()
    
    # Convert to dict
    # brewery_dict = {brewery['id']: brewery for brewery in json_data}
    
    return json_data

def create_map_link(json_data):
    new_data = json_data
    for brewery in json_data:
        street = brewery['address_1']
        city = brewery['city']
        state = brewery['state']
        postal_code = brewery['postal_code']
        address = f'{street} {city} {state}, {postal_code}'
        
        brewery['address'] = address.replace(' ','+')
    print(json_data)

def proper_names(json_data):
    json_data = json_data[0]
    # Create a new dictionary with modified keys
    new_json_data = {}
    for key, value in json_data.items():
        key_new = re.sub(r'[_]+', ' ', key).strip().title()
        new_json_data[key_new] = value
    
    return new_json_data