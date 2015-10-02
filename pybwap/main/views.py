
# -*- coding: utf-8 -*-

import os

import sys

from flask import render_template
from . import main_blueprint

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/static/<folder>/<name>')
def serve(folder, name):
    '''
    Only for developing purpose
    '''
    dirname = os.path.dirname(__file__)
    return send_from_directory(os.path.join(dirname, 'static', folder), filename=name)
