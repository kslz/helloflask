# -*- coding: utf-8 -*-
"""
    @Time : 2022/10/7 18:45
    @Author : 李子
    @Url : https://github.com/kslz
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///')

# 不追踪对象的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
