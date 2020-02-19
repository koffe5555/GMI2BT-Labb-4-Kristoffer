import sqlite3
import requests
from flask import Flask
from random import randint
from flask import Flask, render_template, jsonify
from flask import request

app = Flask(__name__)
# con = sqlite3.connect('databas.db')
# c = con.cursor()

# # c.execute("""CREATE TABLE value (
# #     random1 text,
# #     random2
# # )""")

# # n = randint(1, 999)
# # m = randint(1, 999)
# # a = n, m


# # c.execute("INSERT INTO value (random1, random2) VALUES (?, ?)", a)

# con.commit()
# c.close()

# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/')
def nummer():
    con = sqlite3.connect('databas.db')
    c = con.cursor()
    c.execute('SELECT * FROM databas')
    i = c.fetchall()
    return jsonify(i)

if __name__:
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
