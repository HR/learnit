#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
views.py -
"""

from flask import render_template

from app import app


@app.route('/')
def index():
    """
    Splash page
    """
    return render_template('index.html')


@app.route('/teacher')
def teacher():
    """
    Teacher page
    """
    return render_template('teacher.html')


@app.route('/student')
def student():
    """
    Student page
    """
    return render_template('student.html')
