from flask import Flask,redirect,render_template,jsonify
from flask_bootstrap import Bootstrap5
import requests
import json

app = Flask(__name__)
Bootstrap5(app)


@app.route('/brewery_lookup')
def home(method=['GET']):
    
        
    data = get_single_brewery()
    
    return render_template('brewery_lookup.html',data=data)


def get_single_brewery():
    url = 'https://api.openbrewerydb.org/v1/breweries/random'
    print('Running Data')
    r = requests.get(url)
    json_data = json(r)
    return r.text

