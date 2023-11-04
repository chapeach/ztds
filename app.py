from flask import Flask
from flask_cors import CORS
from my_blueprint import my_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(my_blueprint)

if __name__ == "__main__":
    app.run()