from flask import Flask
import sqlite3
app = Flask(__name__)


###------------- sql statements:
sql_create = """
CREATE TABLE IF NOT EXISTS orders (
  num INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  flavour TEXT,
  quantity INTEGER
);
"""
sql_insert = """INSERT OR IGNORE INTO orders (
  flavour, quantity) values (?,?)""" #num not needed - AI

sql_select = "SELECT * FROM orders"


###------------- on server initialise:
db = sqlite3.connect('orders.db') #create or connect to db
db.cursor().execute(sql_create) #create table if not exists
db.cursor().execute(sql_insert, ("ham & cheese", 5)) #insert tuple
try:
  db.commit() #save
except Exception:
  db.rollback() #crash
finally:
  db.close()


###------------- on application landing:
@app.route("/")
def main():
  html = ""
  try:
    db = sqlite3.connect('orders.db')
    html = str(db.cursor().execute(sql_select).fetchone())
  except Exception as error_msg:
    html = str(error_msg)
  finally:
    db.close()
    return html
    
app.run(debug=True)
