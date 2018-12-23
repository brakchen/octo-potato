from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
app = Flask(__name__)
app.config.from_pyfile('configs.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)



from octo_potato import views, errors, commands
