"""基于Jquery的后台 URL Configuration

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
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginViews.as_view()),
    path('index/', views.index.as_view()),
    path('teacher/', views.teacher.as_view()),
    path('student/', views.student.as_view()),
    path('classes/', views.classes.as_view()),
    path('update_student/', views.Update_student.as_view()),
    path('update_teacher/', views.Update_teacher.as_view()),
    path('update_classes/', views.Update_classes.as_view()),
    path('delete_student/', views.Delete_student.as_view()),
    path('delete_teacher/', views.Delete_teacher.as_view()),
    path('delete_classes/', views.Delete_classes.as_view()),
    path('add_teacher/', views.Add_teacher.as_view()),
    path('add_student/', views.Add_student.as_view()),
    path('add_classes/', views.Add_classes.as_view()),

    path('classes_list/', views.Classes_list.as_view()),


]
