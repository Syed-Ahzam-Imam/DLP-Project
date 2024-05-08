import json
from flask import Flask, jsonify, request
from currencyHelp import *

app = Flask(__name__)
 
 
@app.route('/currency_detection' , methods=['GET'])
def with_parameters_currency_detection():
    url = request.args.get('url')
    prediction=predict(url)
    return jsonify(result=prediction)
 
     
    
if __name__ == '__main__':
    app.run()