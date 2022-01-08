'''
This does the main backend routing
Should be imported from __init__.py to set up all of the routes for the site
'''

from flask import render_template, request, redirect, make_response
from flaskr import app, manager
from flaskr.item import Item
import csv
from io import StringIO


'''
Because we use pagination on the list of items, the {URL}/?page={A NUMBER} syntax is a little sloppy
so instead we will force a redirect to the item_list route
'''
@app.route('/',methods=['GET'])
def home():
    return redirect('/item_list')


'''
ask our database manager for the page passed in the URL arguments
we'll then return the relevant pages
actual db pagination functionality is in another place, keeping the routes file brief is very important
'''
@app.route('/item_list',methods=['GET'])
def item_list():
    page = int('0' if request.args.get('page') == None else request.args.get('page'))
    items = manager.get_page(page)
    return render_template('home.html',items=items)

'''
asks the manager to delete an item with the id given in the URL arguments,
again kept brief to minimize routes file length
'''
@app.route('/delete_item',methods=['GET'])
def delete_item():
    id_ = int(request.args.get('id'))
    manager.delete_item(id_)
    return redirect('/')

'''
creates a new item with default fields
then redirects to the edit page to allow the user to edit their new item
'''
@app.route('/create_item',methods=['GET'])
def create_item():
    id_ = manager.create_item()
    return redirect('/edit_item?id='+str(id_))

'''
the CSV download functionality
The simplest way to do this is just to write the csv file to a stringIO object, bypassing the need to access the disk,
increasing speed by a large amount. Obviously, if massive amounts of inventory exceeding RAM need to be exported, this solution will need to change,
however exporting quickly, to me at least, seems like a good goal.
'''
@app.route('/download',methods=['GET'])
def download():
    csv_str = manager.to_csv()
    si = StringIO()
    cw = csv.writer(si)
    cw.writerows(csv_str)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=inventory.csv"
    output.headers["Content-type"] = "text/csv"
    return output


'''
allows us to edit an item
using a route allowing both get and post requests to minimize the number of unique routes to worry about
The post request simply creates a new Item object based on the data in the form and uses the manager to update the relevant item
the get request just finds the goal item and renders the HTML to edit it.
'''
@app.route('/edit_item',methods=['POST','GET'])
def edit_item():
    if request.method == 'POST':
        id_ = int(request.args.get('id'))
        item = Item(
            id_,
            name = request.form['name'],
            description=request.form['description'],
            quantity=int(request.form['quantity']),
            unit_value=int(request.form['unit_value'])
        )
        manager.edit_item(id_,item)
        return redirect('/')
    elif request.method == 'GET':
        id_ = int(request.args.get('id'))
        item = manager.get_item(id_)
        return render_template('edit.html',item=item)

