from . import views
from django.urls import path

urlpatterns = [
   path('', views.main, name='main-page'),
   path('project/<str:pk>', views.project, name='curr-project')
]
