from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello, %user_name%! <a href="/status">Click here to check server status</a>'


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Snail Messenger',
        'time': str(datetime.now())
    }


app.run()
