#!/usr/bin/env python

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

"""
# https://www.pluralsight.com/guides/manipulating-lists-dictionaries-python
# A list is a mutable, ordered sequence of items.
# list = ['a', 'b', 'c']
# list[0]
# A dictionary is a mutable, unordered set of key-value pairs where each key must be unique.
# dictionary = {}
# In Python, a dictionary is an unordered collection of items. For example:
#  dictionary = {'key' : 'value', 'key_2': 'value_2'}
#  dictionary['key']
"""

# Fake restaurants
restaurants = [
    {'name': 'The CRUDdy Crab'},    # 'id': '0'
    {'name': 'Blue Burger'},        # 'id': '1'
    {'name': 'Taco Hut'}            # 'id': '3'
]

# >>> print(restaurants)
# [{'name': 'The CRUDdy Crab'}, {'name': 'Blue Burger'}, {'name': 'Taco Hut'}]
# >>>
# >>> print(restaurants[0])
# {'name': 'The CRUDdy Crab'}
# >>>
# >>> print(restaurants[0]['name'])
# The CRUDdy Crab
# >>>


# Fake Menu Items
items = [ 
{'name': 'Cheese Pizza', 'description': 'made with fresh cheese',
          'price': '$5.59', 'course': 'Entree'},    # , 'id': '0'
{'name': 'Cheese Pizza2', 'description': 'made with fresh cheese2',
          'price': '$6.59', 'course': 'Entree2'},    # , 'id': '1'
{'name': 'Cheese Pizza3', 'description': 'made with fresh cheese3',
          'price': '$7.59', 'course': 'Entree3'},    # , 'id': '2'
{'name': 'Cheese Pizza4', 'description': 'made with fresh cheese4',
          'price': '$8.59', 'course': 'Entree4'},    # , 'id': '3'
           ]

@app.route('/restaurant/')
@app.route('/')
def showRestaurant():
    # RESTAURANT HOME PAGE
    return render_template('restaurant.html', restaurantx = restaurants)

@app.route('/restaurant/<int:restid>/edit/<string:restname>', methods=['GET','POST'])
def editRestaurant(restid, restname):
    # EDIT RESTAURANT HOMEPAGE
    # https://hackersandslackers.com/flask-routes/
    if request.method == 'POST':
        restname = request.form.get('name')
        restid = request.form.get('id')
        restid0 = int(restid)
        restaurants[restid0]['name'] = restname
    return render_template('editrestaurant.html', restid = restid, restname = restname)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=5000)
