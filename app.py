from flask import Flask, redirect, url_for, render_template, request, flash
import os
import json
app = Flask(__name__, static_folder="static")

@app.route('/collection.html')
def collection():
    with open('data.json', 'r') as file:
        pages = json.load(file)
    return render_template('collection.html', pages=pages)

@app.route('/collection.html/<int:page_id>')
def page(page_id):
    with open('data.json', 'r') as file:
        pages = json.load(file)
    return render_template('page.html', page=pages[page_id])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)