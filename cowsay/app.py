from flask import Flask, jsonify
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_accept import accept, accept_fallback
from cowsay_py import cowsay

app = Flask(__name__)
Bootstrap(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True

app.config['FLASK_DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = False


@app.route('/')
def index():
    cow = cowsay("The Premier CowSay Service")
    return render_template('index.html', message="cowsay.cloud", cow=cow)


@app.route('/say')
@app.route('/say/<message>')
@accept("text/html")
def say(message="moo"):
    cow = cowsay(message)
    return render_template('say.html', message=message, cow=cow)


@say.support("application/json")
def say_json(message="moo"):
    cow = cowsay(message)
    ret = {"message": cow.split('\n')}
    return jsonify(ret)


@say.support("text/plain")
def say_json(message="moo"):
    return cowsay(message)





if __name__ == '__main__':
    app.run()
