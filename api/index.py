from flask import Flask
#from datetime import timedelta

from login import *
#from home import *
#from check_act import *

app = Flask(__name__)

#app.secret_key = "1234"
#app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/')
def home():
    return '7'

app.register_blueprint(login)
#app.register_blueprint(home)
#app.register_blueprint(check_act)

if __name__ == "__main__":
    app.run()
#    app.run(debug=True, host="0.0.0.0")