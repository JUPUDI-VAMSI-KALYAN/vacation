from flask import render_template, request
import os



def index():
    return render_template('index.html')
