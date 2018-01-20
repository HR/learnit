#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main.py - Run python application
"""

from __init__ import *
from app import app
from views import *


def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()
