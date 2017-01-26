from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

from cowsay_py import cowsay

app = Flask(__name__)
Bootstrap(app)

# Because we're security-conscious developers, we also hard-code disabling
# the CDN support (this might become a default in later versions):
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

app.config['FLASK_DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/say')
@app.route('/say/<message>')
def say(message="moo"):
    cow = cowsay(message)
    return render_template('cow.html', message=message, cow=cow)


if __name__ == '__main__':
    app.run()
