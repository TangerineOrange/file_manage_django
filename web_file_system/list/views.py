from django.shortcuts import render
from .models import image
from django.http import HttpResponse
import sys

from django.db.utils import IntegrityError
# 引入我们创建的表单类
from .forms import AddForm
import os
import logging
import json
from django.http import JsonResponse


# Create your views here.

def getList(request):
    return render(request, 'list.html')

def home(request):
    print('home')
    return render(request, 'home.html')

def addAllImgToSQL(request):
    img_root = os.getcwd()+'\common_static\images\\'
    print('getcwd ',img_root)
    print(__file__)
    print(os.path.dirname(__file__))

    dataList=[]

    for file in os.listdir(img_root):
        dataList.append(
            image( name=file, path=img_root+file,type=os.path.splitext(file)[1]))
     
    try:
        image.objects.bulk_create(dataList)
        return HttpResponse("插入成功")
    except Exception as err:
        logging.warning(('post_error', str(err)))
        return HttpResponse("插入失败"+"OS error: {0}".format(err))


def removeAllDataInImage(request):
    try:
        image.objects.all().delete()
        return HttpResponse("删除成功")
    except Exception as err:
        logging.warning(('post_error', str(err)))
        return HttpResponse("删除失败"+"OS error: {0}".format(err))
    

def showAllImageData(request):
    num = '123123'
    images = image.objects.all()
    a = []
    for img in images:
        b= {
            'name': img.name,
            'path': img.path,
            'type': img.type,
        }
        a.append(
            b
        )

    print('a',a)
    print('json',json.dumps(a))
    
    # return render(request, 'home.html', {'num': num})
    return JsonResponse(json.dumps(a),safe=False)
    # return HttpResponse(num)


def login(request):
    if request.method == 'POST':# 当提交表单时
       
        form = AddForm(request.POST) # form 包含提交的数据
         
        if form.is_valid():# 如果提交的数据合法
            name = form.cleaned_data['name']
            path = form.cleaned_data['path']
            return HttpResponse("name: %s , path: %s ." % (name, path))
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'login.html', {'form': form})


# Item.objects.create(name="abc", path="test")

def insertImage(request):

    try:
        image.objects.create(
            id=1,
            name="XIAOWANG",
            path="TEST",
            type=".jpg",
        )
        return HttpResponse("插入成功")
    except IntegrityError as err:
        print("OS error: {0}".format(err))
        return HttpResponse("插入失败"+"OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return HttpResponse("插入失败"+str(sys.exc_info()[0]))

