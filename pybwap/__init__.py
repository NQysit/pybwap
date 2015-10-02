
# -*- coding: utf-8 -*-

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

from .main import main_blueprint
app.register_blueprint(main_blueprint)

from .ch_0x00 import ch_0x00_blueprint
app.register_blueprint(ch_0x00_blueprint)

from .xss_0x01 import xss_0x01_blueprint
app.register_blueprint(xss_0x01_blueprint)
