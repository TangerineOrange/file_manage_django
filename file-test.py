#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pathlib import Path
import os
from sql_utils import insertManyData

files = '\\images\\'


root = os.getcwd()+files

def file_extension(path): 
    return os.path.splitext(path)[1] 

list = []


# print(' a ',type(a))
# print(' list ',type(list))
 
# sdfsdfsdfsdfsdfsdfsdf
# print(' list ',type(val[0]))
# print(' list ',val)
# print(' list ',list(val))


for name in os.listdir(root):
    item = []
    item.append(name)
    item.append(root+name)
    item.append(os.path.splitext(name)[1])
    list.append(tuple(item))

tName = 'images'
insertManyData(tName,list)
print('list ',list[0:5])


