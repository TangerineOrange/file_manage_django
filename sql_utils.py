#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pathlib import Path
import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="frank",
    passwd="123",
    database="frank_test1",
)

def conn():
    mydb = mysql.connector.connect(
        host="localhost",
        user="frank",
        passwd="123",
        database="frank_test1",
    )
    return mydb


def isExist(name):
    mycursor = mydb.cursor()
    sqlselect = "show tables"
    mycursor.execute(sqlselect)
    tablerows = mycursor.fetchall()
    for table in tablerows:
        for t in table:
            if name == t:
                return True
    return False




def insertData(tName,list):
    conn()
    mycursor = mydb.cursor()
    sql = "INSERT INTO %s (name, path ,type) VALUES (%s, %s, %s)"
    val = (tName,"RUNOOB", "https://www.runoob.com")
    mycursor.execute(sql, val)
    mycursor.execute("CREATE TABLE file_list (id int PRIMARY KEY,name VARCHAR(255), url VARCHAR(255),tpye VARCHAR(255))")


def insertManyData(tName,list):
    mydb = conn()
    mycursor = mydb.cursor()
    sql = "INSERT INTO "+tName+" (name, path ,type) VALUES ( %s, %s, %s);"
    mycursor.executemany(sql,list)
    mydb.commit()


val = [
  ('test5', 'test5', 'test5'),
  ('test6', 'test6', 'test6'),
  ('test7', 'test7', 'test7'),
]


tName = "images"


