{"filter":false,"title":"urls.py","tooltip":"/mag/urls.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":15,"column":0},"end":{"row":17,"column":60},"action":"insert","lines":["if settings.DEBUG:","    urlpatterns += static(settings.MEDIA_URL,","                          document_root=settings.MEDIA_ROOT)"],"id":29}],[{"start":{"row":15,"column":0},"end":{"row":17,"column":60},"action":"remove","lines":["if settings.DEBUG:","    urlpatterns += static(settings.MEDIA_URL,","                          document_root=settings.MEDIA_ROOT)"],"id":30}],[{"start":{"row":13,"column":45},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":14,"column":0},"end":{"row":14,"column":6},"action":"insert","lines":["      "]}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":83},"action":"insert","lines":["   url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),"],"id":32}],[{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":33}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":32},"action":"insert","lines":["from .settings import MEDIA_ROOT"],"id":34}],[{"start":{"row":7,"column":28},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":35}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":31},"action":"insert","lines":["from django.views import static"],"id":36}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":0},"end":{"row":18,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1585327159049,"hash":"6a7642590bbfc2a7e988bf7877fc49a70fcfa765"}