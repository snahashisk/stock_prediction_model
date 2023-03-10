import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/name')
def hello_name():
    return 'My name is Snahashis Kanrar'


@app.route('/college')
def hello_college():
    return 'My college name is Dream Institute of Technology'


@app.route('/career')
def hello_career():
    return 'I want to be a Web Developer'


@app.route('/plot')
def hello_plot():
    data = pd.read_csv('sample.csv')
    json_data = data.to_json()
    return json_data


if __name__ == '__main__':
    app.run()
