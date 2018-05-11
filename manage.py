#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: Henry
# @Time: 2018年05月11日20时40分 
# 说明: 
# 总结:


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ihome import create_app, db

app = create_app("develop")

# 创建app管理对象
manage = Manager(app)
Migrate(app, db)
manage.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manage.run()
