from django.shortcuts import render
from .models import Movies
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
from django.http import JsonResponse

# Create your views here.


def insertAllMoviesIntoSQL(request):
    resDir = 'movies/'

    m_root = settings.STATIC_DIR_NAME+resDir

    dataList = []

    for file in os.listdir(m_root):
        dataList.append(
            Movies(
                # number = models.CharField(max_length=30)
                # title = models.TextField()
                # movie_path = models.TextField()
                # cover_name = models.TextField()
                # cover_path = models.TextField()
                # acter = models.CharField(max_length=30)
                # date = models.DateField()
                # publisher = models.CharField(max_length=30)
                # creater = models.CharField(max_length=30)
                # serial = models.TextField()
                
                name=file, path=settings.STATIC_URL+resDir+file, type=os.path.splitext(file)[1]))
        print('file ', file)
        print('path ', settings.STATIC_URL+resDir+file)

    try:
        Movies.objects.bulk_create(dataList)
        return HttpResponse("插入成功")
    except Exception as err:
        logging.warning(('post_error', str(err)))
        return HttpResponse("插入失败"+"OS error: {0}".format(err))


def removeAllDataInMovie(request):
    try:
        Movies.objects.all().delete()
        return "删除成功"
    except Exception as err:
        logging.warning(('post_error', str(err)))
        return "删除失败"+"OS error: {0}".format(err)


def showAllMoviesData():
    movies = Movies.objects.all()
    jsonObj = json.dumps(list(movies.values()))
    print('json', jsonObj)
    return jsonObj
    # return render(request, 'home.html', {'num': num})
    # return JsonResponse(json.dumps(a),safe=False)
    # return HttpResponse(num)


def insertImage(request):
    try:
        Movies.objects.create(
            id=1,
            name="XIAOWANG",
            path="TEST",
            type=".jpg",
        )
        return "插入成功"
    except IntegrityError as err:
        print("OS error: {0}".format(err))
        return "插入失败"+"OS error: {0}".format(err)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return "插入失败"+str(sys.exc_info()[0])
