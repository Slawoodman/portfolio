from . import views
from django.urls import path

app_name = 'blogs'

urlpatterns = [
   path('', views.blog_main, name='blog'),
   path('post/<str:pk>', views.detail, name='detail')
]
