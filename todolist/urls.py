"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from todo.views import TaskList,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='ToDoList'),name='logout'),
    path('',TaskList.as_view(),name='ToDoList'),
    path('create-task/',TaskCreate.as_view(),name='create-task'),
    path('update-task/<int:pk>',TaskUpdate.as_view(),name='update-task'),
    path('delete-task/<int:pk>',TaskDelete.as_view(),name='delete-task')
]
