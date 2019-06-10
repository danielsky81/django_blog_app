"""blog URL Configuration

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
from django.urls import path, re_path
from posts.views import get_todo_list, create_an_item, edit_an_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list),
    path('add', create_an_item),
    path('edit/<int:id>', edit_an_post),
    # or
    # re_path(r'^edit/(?P<id>\d+)$', edit_an_post),
]
