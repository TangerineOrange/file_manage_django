from django.shortcuts import render
from .models import image
from django.http import HttpResponse
import sys

from django.db.utils import IntegrityError
# 引入我们创建的表单类
from .forms import AddForm


# Create your views here.

def getList(request):
    return render(request, 'list.html')

def home(request):
    return render(request, 'home.html')


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

