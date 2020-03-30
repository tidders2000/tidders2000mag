  

from django.conf.urls import url, include
from home.views import index, article


urlpatterns = [
     
    url(r'^$', index, name="index"),
     url(r'^article/', article, name="article"),
]