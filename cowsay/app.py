from flask import Flask
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
    return json.dumps(ret, ensure_ascii=False, indent=2).encode('utf-8')


@say.support("text/plain")
def say_text(message="moo"):
    return cowsay(message).encode('utf-8')





if __name__ == '__main__':
    app.run()
