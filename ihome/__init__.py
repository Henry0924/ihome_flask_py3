#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: Henry
# @Time: 2018年05月11日20时40分 
# 说明: 
# 总结:

import redis
import logging
from flask import Flask
from config import config_dict
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from logging.handlers import RotatingFileHandler

# 创建数据库连接对象
db = SQLAlchemy()

# 创建redis连接对象
redis_store = None

# 补充csrf防护机制
csrf = CSRFProtect()

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)


# 工厂模式
def create_app(config_name):
    """创建项目应用对象"""
    app = Flask(__name__)

    # 获取配置信息
    conf = config_dict.get(config_name)

    app.config.from_object(conf)

    # 初始化
    db.init_app(app)
    csrf.init_app(app)

    global redis_store
    redis_store = redis.StrictRedis(host=conf.REDIS_HOST, port=conf.REDIS_PORT)

    # 将session保存在redis中
    Session(app)

    # 注册蓝图对象
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, prefix="")

    return app
