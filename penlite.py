from flask import Flask, render_template, request, jsonify
import requests
import json
import sunlight
import time
import api_queries

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return render_template("penlight.html")

@app.route('/user_phrase')
def search_function():
    user_phrase = request.args.get('user_phrase')

    query_params = {    
                        'apikey': #INSERT API KEY HERE,
                        'per_page': 5,
                        'phrase': user_phrase,
                        'sort': 'date desc'
                    }

    endpoint = "http://capitolwords.org/api/text.json"
    response = requests.get(endpoint, params=query_params)
    data = response.json()
    information = api_queries.basic_phrase_query(data)

   
    return jsonify({'speakers': information[0], 'quotes': information[1], 'quoteRange': information[2], 'userPhrase': user_phrase})

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
