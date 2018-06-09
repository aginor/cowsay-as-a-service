# Copyright 2017 Andreas Löf <andreas@alternating.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, Response
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_accept import accept_fallback
from cowsay.cowsay_py import cowsay

import json

app = Flask(__name__)
Bootstrap(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True

app.config['FLASK_DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = False


@app.route('/')
def index():
    cow = cowsay("The Premier CowSay Service")
    return render_template('index.html', message="cowsay.io", cow=cow)


@app.route('/say')
@app.route('/say/<path:message>')
@accept_fallback
def say(message="moo"):
    cow = cowsay(message)
    return render_template('say.html', message=message, cow=cow)


@say.support("application/json")
def say_json(message="moo"):
    cow = cowsay(message)
    ret = {"message": cow.split('\n')}
    return Response(json.dumps(ret, ensure_ascii=False, indent=2).encode('utf-8'), mimetype="application/json")


@say.support("text/plain")
def say_text(message="moo"):
    return Response(cowsay(message).encode('utf-8'), mimetype="text/plain")





if __name__ == '__main__':
    app.run()
