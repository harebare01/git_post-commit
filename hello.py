#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/hi')
def hello_world():
    return '<h1>Hello, Build wiht git_post-commit xxxx World!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
