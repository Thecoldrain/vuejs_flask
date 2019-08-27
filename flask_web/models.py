# coding:utf-8
from . import db
import datetime


class User(db.Model):
    '''
    id:用户表主键
    username:用户的登录名
    passwrod: 登录密码需要进行加密
    createTIme:用户创建时间
    email:用户的电子邮箱，这里主要一QQ邮箱和163邮箱为主
    phone:用户电话

    '''
    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(128), index=True, unique=True)  # 用户名
    passwrod = db.Column(db.String(128), nullable=False)  # 用户密码
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())  # 帐号创建时间
    email = db.Column(db.String(128), default=None)
    phone = db.Column(db.Integer, default=None)
    name = db.Column(db.String(128), default=username)

    def __repr__(self):
        return "<User {}>".format(self.username)


class CookieAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("user.username"))
    cookie = db.Column(db.String(4096), nullable=False)

    def __repr__(self):
        return "<CookieAuth {}>".format(self.cookie)
