from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! 1234 app 456 789'

@app.route('/about')
def about():
    return 'About'

#if __name__ == "__main__":
#    app.run(debug=True)