
# -*- coding: utf-8 -*-

import sys
import os

dirname = os.path.dirname(__file__)

class ChallengeAlreadyExist(Exception): pass

if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        ch_name = sys.argv[1]
    
    newdir = os.path.join(dirname, ch_name)
    
    if not os.path.exists(newdir):
        os.makedirs(newdir)
    else:
        raise ChallengeAlreadyExist("{} already exists".format(ch_name))
    
    ch_initpy = open(newdir + '/__init__.py', mode='wt')
    
    ch_initpy.write('''
# -*- coding: utf-8 -*-

from flask import Blueprint

{ch_name}_blueprint = Blueprint('{ch_name}_blueprint', __name__)

from . import {ch_name}'''.format(ch_name=ch_name))

    ch_initpy.close()

    ch_file = open(newdir + '/{ch_name}.py'.format(ch_name=ch_name), mode='wt')
    
    ch_file.write('''
# -*- coding: utf-8 -*-

from flask import render_template

from . import {ch_name}_blueprint

@{ch_name}_blueprint.route('/{ch_name}')
def {ch_name}_view():
    return render_template('{ch_name}.html')'''.format(ch_name=ch_name))
    
    ch_file.close()
    
    
    app_initpy = open(dirname + '/__init__.py', mode='at')
    app_initpy.write('''
from .{ch_name} import {ch_name}_blueprint
app.register_blueprint({ch_name}_blueprint)'''.format(ch_name=ch_name))

    app_initpy.close()
    
    template = open(dirname + '/templates/{ch_name}.html'.format(ch_name=ch_name), mode='wt')
    
    template.write(open(dirname + '/templates/ch_0x00.html', mode='rt').read())
    
    template.close()
    

