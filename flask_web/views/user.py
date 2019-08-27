# coding:utf-8
import json
import re
from .. import app, make_response, request, Blueprint, db,Response,jsonify
import jwt, datetime, time
from ..models import User, CookieAuth
from ..config import parameter
from .tools import loginauth

user = Blueprint("user", __name__)

@user.route("/")
def test():
    return make_response()

# @loginauth
@user.route('/login')
def signIn():
    #  登录
    # 从请求中获取数据
    try:
        cookie = request.headers["cookie"][:-1]
        args_dic = request.args
        username = args_dic['username']
        userpwd = args_dic['userpassword']
        user = User.query.filter_by(username=username).first()
    except Exception as e:
        return jsonify({"error": e})
    # 判断数据是否一致
    if user.username == username and user.passwrod == userpwd:
        response = jsonify()
        try:
            # 判断cookie是否存在 如果不存在则创建一个
            cookie = CookieAuth.query.filter_by(cookie=cookie).first()
        except Exception as e:
            dic = {
                # "headers":header,
                "exp": datetime.datetime.now() + datetime.timedelta(days=7),  # 设置过期时间
                'iat': datetime.datetime.now(),  # 开始时间
                'iss': "flask_web",  # 签名信息
                'data': {
                    "user": username
                }  # 想要传递的数据
            }
            cookie = jwt.encode(dic, "flask_web", algorithm="HS256")
            cookie_t = CookieAuth(cookie=cookie, user_id=username)
            db.session.add(cookie_t)
            db.session.commit()
            response.set_cookie(cookie, max_age=60 * 60 * 24 * 7)
        return jsonify({"sccuess":"测试","测试":'21312'})
    return jsonify({"error": property['login_error']}, 404)


@user.route("/registe", methods=['POST'])
def registe():
    # 注册逻辑
    response = make_response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST"
    response.headers["Access-Control-Allow-Headers"] = "x-requested-with,content-type"

    # request.headers.get("Access-Control-Allow-Origin","*")
    if request.method == 'POST':
        try:
            # response.headers('Access-Control-Allow-Origin','*')
            post = request.form
            username = post['username']
            userpassword = post['userpwd']
            email = post['eamil']
            phone = post['phone']
            name = post['name']

            re_eamil = re.match(r".*\@(163|qq)\.com", email).string
            re_username = re.match(r'(\s|\d|_){6,}', username).string
            re_userpassword = re.match(r'^\w+$', userpassword).string

            re_phone = re.match(r'^1[3|4|5|8][0-9]\d{4,8}$', phone).string
        except Exception as e:
            return response({"error":e})
        try:
            user = User.query.filter_by(username=username).first()
        except Exception as e:
            user = False
        if user:
            return response({"error":"当前用户已被占用"},404)
        re_name = re.match(r'(\s|\d|_)*', name).string
        if not re_name:
            re_name=re_username
        if re_eamil == email and \
                re_username == username and \
                re_name == name and \
                re_userpassword == userpassword \
                and re_phone == phone:
            if not User.query.filter_by(username=username).first():
                user = User(username=username, passwrod=userpassword, email=email, phone=phone, name=name)
                db.session.add(user)
                db.session.commit()
                return response({"success": parameter['create_user_success']}, 200)
    return response({"error": parameter['create_user_error']}, 404)


@user.route('/github')
def github():
    # 第三方github登录认证
    # TODO

    return  make_response({"测试":"s是否有结果"},200)

@user.route("/loginauth")
def signAuth():
    # 认证逻辑
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
        # 重新生成cookie
        dic = {
            # "headers":header,
            "exp": datetime.datetime.now() + datetime.timedelta(days=7),  # 设置过期时间
            'iat': datetime.datetime.now(),  # 开始时间
            'iss': "flask_web",  # 签名信息
            'data': {
                "user": username
            }  # 想要传递的数据
        }
        cookie = jwt.encode(dic, "flask_web", algorithm="HS256")
        cookie_t = CookieAuth(cookie=cookie, user_id=username)
        db.session.add(cookie_t)
        db.session.commit()
        response = jsonify()
        response.set_cookie(cookie, max_age=60 * 60 * 24 * 7)

    return response
