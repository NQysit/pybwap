
# -*- coding: utf-8 -*-

from flask import render_template

from . import ch_0x00_blueprint

@ch_0x00_blueprint.route('/ch_0x00')
def ch_0x00_view():
    return render_template('ch_0x00.html')
