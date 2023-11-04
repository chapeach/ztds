from flask import Flask
from my_blueprint import bp

app = Flask(__name)
app.register_blueprint(bp, url_prefix="/my_blueprint")