#!/usr/bin/env python
"""Website with flask
"""
from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('switcher.html', title="Switch Things")

#@app.route('/hello/')
@app.route('/switch/<name>')
def switch(name=None):
    print name
    return redirect(url_for('main')) 

if __name__ == '__main__':
    app.run()

