from flask import Flask, jsonify, request, url_for, redirect, session, render_template,g
import sqlite3

app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect('User_Gov')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route('/',methods=['GET'])
def index():
    return render_template('login.html')
   
@app.route('/theform',methods=['POST', 'GET'])
def theform():

    if request.method == 'GET':
        return render_template('index_login.html')
    else:
        name = request.form['username']
        password = request.form['password']

        return render_template('infouser.html',name=name)


@app.route('/thevalidate',methods=['POST', 'GET'])
def thevalidate():

        user2add = request.form['user2add']
        primarygrp = request.form['primarygrp']
        secondarygrp = request.form['secondarygrp']
        servers = request.form['servers']

        return '<h1>Hello {}. Welcome to User Governance Page!.<h1>'.format(user2add)


if __name__ == '__main__':
    app.run(debug=True)