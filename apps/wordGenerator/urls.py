from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),### this is going to call the index function under views.py
    url(r'^generate$', views.generate, name='generate'),
    url(r'^reset$', views.reset, name='reset')
]