#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
views.py -
"""

from flask import render_template
from flask import send_from_directory

from app import app

import os

root_dir = os.path.dirname(os.getcwd())
views_root = os.path.join(root_dir, 'app/templates')

# HTTP Errors handlers


@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route('/')
def index():
    """
    Splash page
    """
    return send_from_directory(views_root, 'index.html')


@app.route('/teacher')
def teacher():
    """
    Teacher page
    """
    return send_from_directory(views_root, 'teacher.html')


@app.route('/student')
def student():
    """
    Student page
    """
    return send_from_directory(views_root, 'student.html')
