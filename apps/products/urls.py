__author__ = 'MatthewHan'
from django.conf.urls import patterns, url # import functions to match patterns
from apps.products import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/', views.index, name = 'products'),
    url(r'^create/', views.create, name = 'create'),
    url(r'^products/(?P<product_id>\d+)/$', views.show, name = 'show'),
]