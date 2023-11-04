from flask import Flask
from my_blueprint import bp

app = Flask(__name__)
app.register_blueprint(bp, url_prefix="/my_blueprint")