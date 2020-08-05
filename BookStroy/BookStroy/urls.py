"""BookStroy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    # 管理员账户登陆
    url(r'^admin/', admin.site.urls),
    # 出版社列表
    url(r'^publisher_list/', views.publisher_list),
    # 添加出版社
    url(r'^add_publisher/', views.add_publisher),
    # 删除出版社
    url(r'^drop_publisher/', views.drop_publisher),
    # 修改出版社
    url(r'^edit_publisher/', views.edit_publisher),
    url(r'^book_list/', views.book_list),
    url(r'^add_book/', views.add_book),
    url(r'^drop_book/', views.drop_book),
    url(r'^edit_book/', views.edit_book),
    url(r'^author_list/', views.author_list),
    url(r'^add_author/', views.add_author),
    url(r'^drop_author/', views.drop_author),
    url(r'^edit_author/', views.edit_author),
    url(r'^$', views.publisher_list),  # 只有跟网址，默认匹配
]
