
# -*- coding: utf-8 -*-

from flask import render_template, request

from . import xss_0x01_blueprint

@xss_0x01_blueprint.route('/xss_0x01')
def xss_0x01_view():
    
    name = request.args.get('name', 'World')
    
    return render_template('xss_0x01.html', name=name)
