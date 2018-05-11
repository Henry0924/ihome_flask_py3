#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: Henry
# @Time: 2018年05月11日20时40分 
# 说明: 
# 总结:

import redis


class Config(object):
    SECRET_KEY = "jwwoe29u4u.lm"

    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_py3"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 配置redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 配置flask_session
    SESSION_TYPE = "redis"  # 设置session保存在redis中
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行签名加密
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 创建redis连接对象
    PERMANENT_SESSION_LIFETIME = 86400  # 设置redis的有效时间


class DevelopConfig(Config):
    """开发模式配置信息"""
    DEBUG = True


class ProductConfig(Config):
    """生产模式 线上模式配置信息"""
    pass


config_dict = {
    "develop": DevelopConfig,
    "product": ProductConfig
}
