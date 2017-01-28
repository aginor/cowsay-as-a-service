from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

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
def say(message="moo"):
    cow = cowsay(message)
    return render_template('cow.html', message=message, cow=cow)


if __name__ == '__main__':
    app.run()
