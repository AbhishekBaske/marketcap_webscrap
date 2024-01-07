from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    with open('./company.json', 'r') as f:
        data = json.load(f)
    return render_template('index.html', data=data)

