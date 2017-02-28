from flask import Flask, jsonify

from models.WatsonModel import fetchClassification

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"

@app.route('/fetch')
def view():
    return fetchClassification()




if __name__ == '__main__':
    app.run(debug=True)
