#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/4/30 12:20 上午
# @Author   : vadon
# @File     : post.py
# @Software : PyCharm


from flask import request, Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/test', methods=['POST'])
def post_data():
    print('hh')
    data = request.form['id']
    recognize_info = {'id': data}
    return jsonify(recognize_info), 201


if __name__ == '__main__':
    print('Begin')
    app.run(debug=False, host='localhost', port=8888)
