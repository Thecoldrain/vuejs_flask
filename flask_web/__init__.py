# coding:utf-8
from flask import Flask,session,make_response,request,Blueprint,Response,jsonify
from . import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("flask_web.config")
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from . import models
from views.user import user
