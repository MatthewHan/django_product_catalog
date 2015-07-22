__author__ = 'MatthewHan'
from django.conf.urls import patterns, url # import functions to match patterns
from apps.products.views import ProductsView, ProductView
from apps.products import views
urlpatterns = [
    url(r'^$', ProductsView.as_view()),
    #url(r'^products/', ProductsView.as_view()),
    url(r'^(?P<product_id>\d+)/$', ProductView.as_view()),
    url(r'^(?P<product_id>\d+)/edit', views.edit, name = 'edit'),
    # url(r'^products/(?P<product_id>\d+)/$', Product.as_view(), name = 'product'),
]