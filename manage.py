import os         
import json
import sqlite3
from flask import Flask, render_template, request, g, redirect
from pymongo import Connection

app = Flask(__name__)
connection = Connection()

@app.route('/', methods=['GET', 'POST'])
def paintapp():
    if request.method == 'GET':
        py_all = {}
        db=connection.data
        cur = db.collection
        all_data = cur.find()
        for each in all_data:
            py_all[each["filename"]] = each["imagedata"]
        return render_template('paint.html', file_list=py_all)
    elif request.method == 'POST':
        file_name = request.form['fname']
        data = request.form['img_data']
        db=connection.data
        cur = db.collection	
	cur.insert({"filename":file_name,"imagedata":data})
        return redirect('/')
   
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
