# coding:utf-8
from flask_web import app,db
from flask_web.views.user import user


app.register_blueprint(user, url_prefix="/")

if __name__ == '__main__':
    app.run()
