# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

host = 'admin.cjp8hsqu4je0.us-east-2.rds.amazonaws.com'
user = 'admin'
password = '12345678'
database = 'admin'

connection = pymysql.connect(host, user, password, database)
with connection:
    cur = connection.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    print("Database version: {} ".format(version[0]))
