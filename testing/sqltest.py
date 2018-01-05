from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

db = SQLAlchemy()
# engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:gunjan123@localhost:3306/mysql'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(80))
    email = db.Column('emails', db.String(120))

