from flask import Flask,redirect,render_template,jsonify,request,url_for
from flask_bootstrap import Bootstrap5
import requests
import json
import re
from urllib.parse import urlencode

app = Flask(__name__)
Bootstrap5(app)

# Default URL for Openbrewerydb
DEFAULT_URL = 'https://api.openbrewerydb.org/v1/breweries'

@app.route('/brewery_lookup')
def home():
    data = get_random_breweries()
    headers_list = proper_names(data)
    return render_template('brewery_lookup.html', data=data, headers=headers_list)

@app.route('/search_brew', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        json_data = get_brewery_list(request)
        json_data = create_map_link(json_data)
        headers_list = proper_names(json_data)
        
        return render_template('brewery_lookup.html', data=json_data, headers=headers_list)
    return render_template('search.html')

def get_brewery_list(request = None) -> dict:
    """Query the API based on parameters provided by user and return Json data as results. Also handles creating the map URL link."""
    params = {}
    
    
    if request:
        # Handle form data if request is provided
        if request.method == 'POST':
            b_name = request.form.get('brewName')
            b_city = request.form.get('cityName')
            b_state = request.form.get('stateName')
            if b_name:
                params['by_name'] = b_name
            if b_city:
                params['by_city'] = b_city
            if b_state:
                params['by_state'] = b_state

    
    # Make the API request
    query_string = urlencode(params)
    url = f"{DEFAULT_URL}?{query_string}"
    r = requests.get(url)
    json_data = r.json()
    json_data = create_map_link(json_data)
    
    return json_data
    


def get_random_breweries():
    url = 'https://api.openbrewerydb.org/v1/breweries/random?size=10'
    
    r = requests.get(url)
    print(r.content)
    json_data = r.json()
    # Creates the map link that will be utilized in the HTML code to create a clickable google maps link for users.
    json_data = create_map_link(json_data)
    
    return json_data

def create_map_link(json_data):
    modified_data = json_data.copy()
    for brewery in modified_data:
        street = brewery['address_1']
        city = brewery['city']
        state = brewery['state']
        postal_code = brewery['postal_code']
        address = f'{street} {city} {state}, {postal_code}'
        
        brewery['address'] = address.replace(' ','+')
    return modified_data


def proper_names(json_data):
    json_data = json_data[0]
    # Create a new dictionary with modified keys
    new_json_data = {}
    for key, value in json_data.items():
        key_new = re.sub(r'[_]+', ' ', key).strip().title()
        new_json_data[key_new] = value
    
    return new_json_data