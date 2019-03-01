# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask, request, redirect, make_response, url_for
import os

app = Flask(__name__)


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    # name = request.args.get('name')
    # return '', 302, {'Location', 'https://www.baidu.com'}
    return redirect('https://www.baidu.com')


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/foo')
def foo():
    resp = make_response('hello')
    resp.mimetype = 'text/plain'
    return resp


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, a Human!')


@app.route('/set/<name>')
def set_cook(name):
    res = make_response(redirect(url_for('index')))
    res.set_cookie('name',name)
    return res


@app.route('/key')
def key():
    return os.getenv('SECRET_KEY')