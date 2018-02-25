from flask import Flask, render_template, request
import requests
import json
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)

# One route so far - root
@app.route('/', methods=['GET'])
def index():
    quote_parameters = {
    'types': 'quote'
    }

    if request.method == 'GET':
        try:
            response = requests.get('https://api.iextrading.com/1.0/stock/nvda/batch', params=quote_parameters)
            logo = requests.get('https://api.iextrading.com/1.0/stock/nvda/logo').json()
            data = response.json()
            stock_quote_high = data['quote']['high']
            stock_quote_low = data['quote']['low']
            stock_quote_avg = (stock_quote_high + stock_quote_low) / 2
            stock_quote_avg = str(round(stock_quote_avg, 2))
            print('Stock average is:', stock_quote_avg)
        except:
            print('ERROR')
    return render_template(
        'index.html',
        raw_data=data,
        stock_quote_avg=stock_quote_avg,
        logo=logo
    )
