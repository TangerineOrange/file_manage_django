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
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'login.html', {'form': form})


# Item.objects.create(name="abc", path="test")

def insertImage(request):

    try:
        image.objects.create(
            id=11,
            name="XIAOWANG",
            path="TEST",
            type=".jpg",
        )
        return HttpResponse("插入成功")
    except IntegrityError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        return HttpResponse("插入失败"+str(sys.exc_info()[0]))

