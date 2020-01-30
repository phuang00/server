import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
# imported Flask, render_template, request, redirect, url_for, and session
app = Flask(__name__)
#create instance of class Flask

DIR = os.path.dirname(__file__) or '.'
DIR += '/'

@app.route("/")
def root():
    return render_template("base.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
