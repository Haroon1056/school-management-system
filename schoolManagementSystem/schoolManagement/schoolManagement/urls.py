"""
URL configuration for schoolManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from schoolapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create_student', views.create_student),
    path('add_student', views.add_student),
    path('student_list', views.student_list),
    path('edit/<int:id>', views.edit_student),
    path('update_student/<int:id>', views.update_student),
    path('delete/<int:id>', views.delete_student),
    path('search_student', views.search_student),
    path('create_result', views.create_result),
    path('add_result', views.add_result),
    path('result_list', views.result_list),
    path('delete_result/<int:id>', views.delete_result),
    path('search_result', views.search_result),
    path('create_fee', views.create_fee),
    path('add_fee', views.add_fee),
    path('fee_list', views.fee_list),
    path('delete_fee/<int:id>', views.delete_fee),
    path('search_fee', views.search_fee),
]
