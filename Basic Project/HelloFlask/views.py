"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

   
    return render_template(
     "index.html",
        title = "Hello Flask",
        message = "Hello, Flask!",
        content = " on " + formatted_now)

@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    return render_template(
        "about.html",
        title = "About HelloFlask",
        content = "Example app page for Flask.")

from flask import Flask
import sqlite3


import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    message = ""
    try:
        db = sqlite3.connect('test.db') #creates if not exists already
        cursor = db.cursor()
        cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT);")
        cursor.execute("INSERT INTO users (id,email) values (?, ?)",(99, "me@my.com"))
        db.commit()
        message = "Database was created, and some records were inserted."
    except Exception:
        db.rollback()
        message = "Something went wrong."
    finally:
        db.close()
        return message
    
app.run()
   
@app.route('/sqlite')
def sqlite():
    return render_template(
        "slite.html",
        title = "sqlite HelloFlask",
        content = "Example app page for Flask.")

