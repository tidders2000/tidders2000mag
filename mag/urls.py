
from django.conf.urls import url, include
from django.contrib import admin
from home import urls as urls_home
from .settings import MEDIA_ROOT
from accounts import urls as urls_accounts
from advert import urls as urls_advert
from home.views import index
from django.views import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^$', index, name='index'),
     url(r'^home/', include(urls_home)),
      url(r'^advert/', include(urls_advert)),
         url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
