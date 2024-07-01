import functions_framework
import requests
import os
from flask import jsonify

API_KEY = ""

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'text' in request_json:
        text = request_json['text']
    elif request_args and 'text' in request_args:
        text = request_args['text']
    else:
        return jsonify({'error': 'Please provide text in the request body or as a query parameter'}), 400

    # Prepare the request payload
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": text
        },
        "encodingType": "UTF8"
    }

    # Make the API request
    url = f"https://language.googleapis.com/v1/documents:analyzeSentiment?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to analyze sentiment', 'details': response.text}), 500

    return jsonify(response.json())
