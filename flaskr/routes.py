from flask import render_template, request, redirect, make_response
from flaskr import app, manager
from flaskr.item import Item
import csv
from io import StringIO

@app.route('/',methods=['GET'])
def home():
    return redirect('/item_list')

@app.route('/item_list',methods=['GET'])
def item_list():
    page = int('0' if request.args.get('page') == None else request.args.get('page'))
    items = manager.get_page(page)
    return render_template('home.html',items=items)

@app.route('/delete_item',methods=['GET'])
def delete_item():
    id_ = int(request.args.get('id'))
    manager.delete_item(id_)
    return redirect('/')

@app.route('/create_item',methods=['GET'])
def create_item():
    id_ = manager.create_item()
    return redirect('/edit_item?id='+str(id_))

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

