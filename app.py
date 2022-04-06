from flask import Flask, request, render_template
from search_engine import search_engine
import requests
import json
from urllib.request import urlopen
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)

@app.route('/')
def index():
    global city
    try:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)

        IP=data['ip']
        org=data['org']
        city = data['city']
        country=data['country']
        region=data['region']
    except:
        city = "Cambridge , Massachusetts News"

    return render_template('index.html', location=city)


@app.route('/search',methods=['GET'])
def search():
    query = request.args.get('query')
    search_results = search_engine.search_func(query=f"{query} {city}")
    if not search_results:
        return no_results_template(query)
    return render_template('search_results.html', search_results=search_results, query=query)

@app.route('/map')
def mymap():
    return render_template('map.html', mymap=mymap)

def no_results_template(query):
    return render_template('simple_message.html', title='No results found',
                           message='Your search - <b>' + query + '</b> - did not match any documents.'
                                                                 '<br>Suggestions:<br><ul>'
                                                                 '<li></li>'
                                                                 '<li>Try different keywords.</li>'
                                                                 '<li>Try more general keywords.</li>'
                                                                 '<li>Try fewer keywords.</ul>')