from flask import Flask, request, render_template
from search_engine import search_engine
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    global city
    # ip_addr = request.remote_addr
    # print(f"User's IP {ip_addr}")
    # url = 'http://freegeoip.net/json'
    # r = requests.get(url)
    # print(r)
    # j = json.loads(r.text)
    # city = j['city']
    city = "Cambridge MA"
    return render_template('index.html')


@app.route('/search',methods=['GET'])
def search():
    query = request.args.get('query')
    search_results = search_engine.search_func(query=f"{query} {city}")
    if not search_results:
        return no_results_template(query)
    return render_template('search_results.html', search_results=search_results, query=query)

def no_results_template(query):
    return render_template('simple_message.html', title='No results found',
                           message='Your search - <b>' + query + '</b> - did not match any documents.'
                                                                 '<br>Suggestions:<br><ul>'
                                                                 '<li></li>'
                                                                 '<li>Try different keywords.</li>'
                                                                 '<li>Try more general keywords.</li>'
                                                                 '<li>Try fewer keywords.</ul>')