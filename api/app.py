from flask import flask
app = Flask(__name__)

def index():
    return('hello')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')