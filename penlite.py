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
    return render_template("state.html")

@app.route('/user_phrase')
def phrase_search_function():
    user_phrase = request.args.get('user_phrase')

    query_params = {    
                        'apikey': 'ed7d3072124947d1b3fdf8fb1e89e61f',
                        'per_page': 5,
                        'phrase': user_phrase,
                        'sort': 'date desc'
                    }

    endpoint = "http://capitolwords.org/api/text.json"
    response = requests.get(endpoint, params=query_params)
    data = response.json()
    information = api_queries.basic_phrase_query(data)

   
    return jsonify({'speakers': information[0], 'quotes': information[1], 'quoteRange': information[2], 'userPhrase': user_phrase})

@app.route('/user_state')
def state_search_function():
    user_state = request.args.get('user_state')

    query_params = {    
                        'apikey': 'ed7d3072124947d1b3fdf8fb1e89e61f',
                        'per_page': 10,
                        'entity_type': 'state',
                        'entity_value': user_state
                    }

    endpoint = "http://capitolwords.org/api/phrases.json"
    response = requests.get(endpoint, params=query_params)
    data = response.json()

    information = api_queries.top_words_by_state(data)
    return jsonify(information)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
