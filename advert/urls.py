from django.conf.urls import url, include
from .views import advert, SearchResultsView, advertview, error

urlpatterns=[
    url(r'^advert/',advert, name='advert'),
     url(r'^search/', SearchResultsView, name='search_results'),
       url(r'^error/', error, name='error'),
      url(r'advertview/(?P<id>[0-9]+)$', advertview, name='advertview'),
   
    ]