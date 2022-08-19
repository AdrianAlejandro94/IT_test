import requests
import json
import yahoofinantials, database
from flask import Flask, request, json

url = 'https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9'  # URL to Webhooks

data = yahoofinantials.get_yahoo_data()  # get data from yahoo
database.store_database(data)  # store in database

api = Flask(__name__)  # Flask API


@api.route('/exchange', methods=['GET'])  #API get exchange from database by date
                                          # example: http://localhost:5000/exchange?date=2022-08-04
def get_exchanges():
    """
    Method Get Exchange from database by date and POST to webHooks the result
    :return:
    """
    date = request.args.get('date')  # Get Date in param from request
    result = database.exchange(date)  # Get record from database
    requests.post(url, json=result)   # Post to Webhooks the record queried
    return json.dumps(result)


if __name__ == '__main__':
    api.run(host='localhost', port=5000)  # run server in localhost port 5000
