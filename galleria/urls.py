from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\d+)',views.location_filter,name ='location')
]