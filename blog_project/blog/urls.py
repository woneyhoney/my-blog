from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    # <어떤 타입으로 계층적 url 설계?:detail 함수로 넘어가는 인자> 안에 내용 - path converter 
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),
    path('search/', views.search, name="search"),
]