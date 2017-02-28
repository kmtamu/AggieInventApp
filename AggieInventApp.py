from flask import Flask, jsonify
from flask import render_template
from flask import request

from models.WatsonModel import fetchClassification

import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

    #return "Hello"

@app.route('/fetch')
def view():
    print(searchterm)
    return fetchClassification()




@app.route('/getfile',methods=['POST'])
def addRegion():
    print("I got it!")
    print(request.form['myFile'])
    return render_template('some.html', data=request.form['myFile'])




if __name__ == '__main__':
    app.run(debug=True)
