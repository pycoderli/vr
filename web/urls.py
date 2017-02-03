"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from inventory import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^house_detail/(?P<id>\d+)/', views.house_detail, name='house_detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^panorama/', views.panorama, name='panorama'),
    url(r'^room_pic/(?P<id>\d+)/', views.room_pic, name='room_pic'),
    url(r'^arrow_pic/(?P<id>\d+)/', views.arrow_pic, name='arrow_pic')
]
