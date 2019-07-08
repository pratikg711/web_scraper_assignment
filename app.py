"""
Created By  : Pratik 
Created At  : 8 Jul 2019
Description : Amazon web scraper
"""

from flask import Flask, request, jsonify, render_template,send_file
import json
import os
import pprint
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config["DEBUG"] = True

html_source = os.path.join(os.path.dirname(os.path.realpath(__file__)), "aws_list.html")



# get_prouducts() : get product price and its name
@app.route('/api/v1/resources/getProduct', methods=['GET'])
def get_products():
    if 'product_name' in request.args:
        product_name = request.args['product_name']
    else:
        return jsonify({ "status": "200","data" : "Please specify product!" })

    data_file = read_html_source(html_source)
    soup = BeautifulSoup(data_file,"html.parser")
    product_array = []
    for i in range(len(soup.findAll("span", class_="a-price-whole"))): 
        price = {}
        name = {}
        product = {}
        try:
            price = soup.findAll('span', class_="a-price-whole")[i]
            name = soup.findAll('span', class_="a-size-base-plus a-color-base a-text-normal")[i]
            product["price"] = "Rs." + price.text
            product["name"] = name.text
            product_array.append(product)
        except:
            continue

    response = {}
    response['product_details'] = product_array
    
    return jsonify(response)

# Reading the data from file
def read_html_source(html_source):
    try:
        fp = open(html_source, encoding="utf8") 
        data = fp.read()
        return data
    except:
        return jsonify("Error in reading html file")

# Running the application on localhost:8888
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)

#Handling for invalid routes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": "404", "data": "Page Not Found!"})