# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 4:24 下午
# @Author   : vadon
# @Email    : vadonical@gmail.com
# @File     : flask_cbv.py
# @Project  : proxymask


from flask import Flask, views, render_template, send_file, request, session

app = Flask(__name__)

app.secret_key = "test hello world"


class Login(views.MethodView):
    decorators = ['get', 'post', 'head', 'options', 'delete', 'put', 'trace', 'patch']

    def get(self):
        return render_template("login.html")

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'one' and password == '111':
            session['username'] = 'one'
            return 'ok'
        return 'error'


app.add_url_rule('/login', view_func=Login.as_view(name='login'))

if __name__ == '__main__':
    app.run()
