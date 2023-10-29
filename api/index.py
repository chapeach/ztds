from flask import Flask
from datetime import timedelta

from login import *
from home import *

app = Flask(__name__)

app.secret_key = "1234"
app.permanent_session_lifetime = timedelta(minutes=30)

app.register_blueprint(login)
app.register_blueprint(home)

#if __name__ == "__main__":
#    app.run(debug=True, host="0.0.0.0")