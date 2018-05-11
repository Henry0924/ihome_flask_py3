#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: Henry
# @Time: 2018年05月11日20时40分 
# 说明: 
# 总结:

from flask import Blueprint

# 创建蓝图对象
api = Blueprint("api_1_0", __name__)

# 导入视图函数
from .index import index
