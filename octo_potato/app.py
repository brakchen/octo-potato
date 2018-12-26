import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
db = SQLAlchemy(app)

class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(70), unique=True)
    phone = db.Column(db.String(20))
    articles = db.relationship('Article')

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),index=True)
    body= db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))








app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:////'+ os.path.join(app.root_path, 'data.db'))

@app.cli.command()
def initdb():
    db.create_all()

# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.cli.command()
def hello():
    click.echo("hello")

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,author=Author, article=Article)
