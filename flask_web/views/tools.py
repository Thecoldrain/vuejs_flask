# coding:utf8
import datetime

import jwt
from flask import request, make_response,jsonify

from flask_web import db
from flask_web.config import parameter
from flask_web.models import CookieAuth, User


def loginauth(func):
    def signAuth():
        try:
            cookie = request.headers["cookie"][:-1]
            # CookieAuth.query.filter_by(cookie=cookie, user).first()
            service_cookie = CookieAuth.query.filter_by(cookie=cookie).first().cookie
        except Exception as e:
            return jsonify({'error': e}, 404)
        if cookie != service_cookie or cookie == None:
            return
        dic = jwt.decode(cookie, "flask_web", algorithms="HS256")
        outtime = dic["exp"]
        username = dic.get("data")["user"]

        name = User.query.filter_by(username=username).first()
        if username != name and username == None and name == None:
            return jsonify({"error": parameter['signauth_error']})

        if outtime <= datetime.datetime.now() + datetime.timedelta(days=7):
            # 超过七天自动清除服务器中的cookie
            service_cookies = CookieAuth.query.filter_by(cookie=cookie).first()
            db.session.delete(service_cookies)
            db.session.commit()
            # 装饰器中不胜成cookie需要重新登录创建新的cookie，前端js在这次返回结果中删除web中的cookie
            # 重新生成cookie
            # dic = {
            #     # "headers":header,
            #     "exp": datetime.datetime.now() + datetime.timedelta(days=7),  # 设置过期时间
            #     'iat': datetime.datetime.now(),  # 开始时间
            #     'iss': "flask_web",  # 签名信息
            #     'data': {
            #         "user": username
            #     }  # 想要传递的数据
            # }
            # cookie = jwt.encode(dic, "flask_web", algorithm="HS256")
            # cookie_t = CookieAuth(cookie=cookie, user_id=username)
            # db.session.add(cookie_t)
            # db.session.commit()
            # response = jsonify()
            # response.set_cookie(cookie, max_age=60 * 60 * 24 * 7)
            return jsonify({"url":"index"})

        return func()
    return signAuth