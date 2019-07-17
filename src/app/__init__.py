import flask
from os import getenv

app = flask.Flask(__name__)

app.config['HOST'] = getenv('HOST', '127.0.0.1')
app.config['PORT'] = getenv('PORT', '5000')

from . import views
