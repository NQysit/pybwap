
# -*- coding: utf-8 -*-


from flask import render_template, send_from_directory
from . import main_blueprint

@main_blueprint.route('/')
def index():
    return render_template('index.html')


