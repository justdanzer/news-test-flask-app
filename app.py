from flask import Flask, request, render_template
from search_engine import search_engine
import requests
import json
from urllib.request import urlopen
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from newsapi import NewsApiClient
import const

app = Flask(__name__)

@app.route('/')
def index():
    global city
    global IP
    global org
    global city
    global country
    global region
    try:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        print(data)
        IP=data['ip']
        org=data['org']
        city = data['city']
        country=data['country']
        region=data['region']
    except:
        city = "Cambridge"
        region = "Massachusetts"
        country = "US"

    return render_template('index.html', location=f"{city} {region} {country}")

@app.route('/topstories')
def topstories():
    newsapi = NewsApiClient(api_key='0d09928cab5c4623bd3a1de740dd2a67')
    search_results = newsapi.get_everything(q=f"News {city} {region} {country}",  page_size=10)
    return render_template('top_stories.html', search_results=search_results['articles'])

@app.route('/search',methods=['GET'])
def search():
    query = request.args.get('query')
    newsapi = NewsApiClient(api_key='0d09928cab5c4623bd3a1de740dd2a67')
    search_results = newsapi.get_top_headlines(q=query)
    if not search_results:
        return no_results_template(query)
    return render_template('search_results.html', search_results=search_results['articles'], query=query)

@app.route('/map')
def mymap():
    map = GoogleMaps(app)
    return render_template('map.html', mymap=map)



def no_results_template(query):
    return render_template('simple_message.html', title='No results found',
                           message='Your search - <b>' + query + '</b> - did not match any documents.'
                                                                 '<br>Suggestions:<br><ul>'
                                                                 '<li></li>'
                                                                 '<li>Try different keywords.</li>'
                                                                 '<li>Try more general keywords.</li>'
                                                                 '<li>Try fewer keywords.</ul>')