# coding:utf-8
from flask import Flask, session, make_response, request, Blueprint, Response, jsonify
from . import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import *

app = Flask(__name__)
CORS(app)
app.config.from_object("flask_web.config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models
from flask_web.views.user import user
