from django.shortcuts import render
from .models import image
from django.http import HttpResponse
import sys

from django.db.utils import IntegrityError
# 引入我们创建的表单类
from .forms import AddForm
from django.conf import settings
import os
import logging
import json
from . import operate_images_sql
from . import operate_movies_sql
from django.http import JsonResponse

# Create your views here.

def getList(request):
    return render(request, 'list.html')

def home(request):
    print('home')
    return render(request, 'home.html')

def movies(request):
    return render(request, 'movies.html')

def addAllImgToSQL(request):
    print('static',settings.STATICFILES_DIRS)
    print('static',settings.STATIC_URL)
    resDir = 'images/'
    
    # img_root = os.getcwd()+'\common_static\images\\'
    # print(__file__)
    # print(os.path.dirname(__file__))
    print('getcwd 2',os.getcwd())

    img_root = settings.STATICFILES_DIRS[0]+resDir

    dataList=[]

    for file in os.listdir(img_root):
        dataList.append(
            image( name=file, path=settings.STATIC_URL+resDir+file,type=os.path.splitext(file)[1]))
        print('file ',file)
        print('path ',settings.STATIC_URL+resDir+file)
        
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
    # return JsonResponse(json.dumps(a),safe=False)
    return JsonResponse(a,safe=False)
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





def showAllMoviesData(request):
    return HttpResponse(operate_movies_sql.showAllMoviesData())

def insertAllMoviesIntoSQL(request):
    return HttpResponse(operate_movies_sql.showAllMoviesData())
