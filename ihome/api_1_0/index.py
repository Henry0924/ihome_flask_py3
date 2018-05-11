#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: Henry
# @Time: 2018年05月11日20时41分 
# 说明: 
# 总结:

import logging
from . import api


@api.route("/index")
def index():
    logging.error("error msg")
    logging.warning("warn msg")
    logging.info("info msg")
    logging.debug("debug msg")

    return "INDEX PAGE ihome_flask_py3"
