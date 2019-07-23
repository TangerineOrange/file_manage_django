"""web_file_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from list import views  as list_views


urlpatterns = [
    path('showAllMoviesData/',list_views.showAllMoviesData,name='showAllMoviesData'),

    
    path('showAllImageData/',list_views.showAllImageData,name='showAllImageData'),
    path('addAllImgToSQL/',list_views.addAllImgToSQL,name='addAllImgToSQL'),
    path('removeAllDataInImage/',list_views.removeAllDataInImage,name='removeAllDataInImage'),

    path('',list_views.movies,name='movies'),
    path('',list_views.home,name='home'),

    path('list/',list_views.getList,name='list'),
    path('login/',list_views.login,name='login'),
    path('insertImage/',list_views.insertImage,name='insertImage'),
    path('admin/', admin.site.urls),
]
