{"filter":false,"title":"settings.py","tooltip":"/mag/settings.py","undoManager":{"mark":22,"position":22,"stack":[[{"start":{"row":41,"column":4},"end":{"row":41,"column":6},"action":"insert","lines":["''"],"id":82}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["s"],"id":83},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["t"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["o"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["r"]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["a"]},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["g"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["e"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":[","],"id":84}],[{"start":{"row":135,"column":0},"end":{"row":145,"column":69},"action":"insert","lines":["AWS_S3_OBJECT_PARAMETERS = {","    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl':'max-age=94608000',","    ","}","AWS_STORAGE_BUCKET_NAME = 'jessbutler-media'","AWS_S3_REGION_NAME = 'us-east-1'","AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')","AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')","","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'% AWS_STORAGE_BUCKET_NAME"],"id":85}],[{"start":{"row":140,"column":31},"end":{"row":140,"column":36},"action":"remove","lines":["butle"],"id":86},{"start":{"row":140,"column":28},"end":{"row":140,"column":33},"action":"insert","lines":["butle"]}],[{"start":{"row":140,"column":36},"end":{"row":140,"column":37},"action":"remove","lines":["r"],"id":87},{"start":{"row":140,"column":35},"end":{"row":140,"column":36},"action":"remove","lines":["s"]},{"start":{"row":140,"column":34},"end":{"row":140,"column":35},"action":"remove","lines":["s"]},{"start":{"row":140,"column":33},"end":{"row":140,"column":34},"action":"remove","lines":["e"]},{"start":{"row":140,"column":32},"end":{"row":140,"column":33},"action":"remove","lines":["e"]},{"start":{"row":140,"column":31},"end":{"row":140,"column":32},"action":"remove","lines":["l"]},{"start":{"row":140,"column":30},"end":{"row":140,"column":31},"action":"remove","lines":["t"]},{"start":{"row":140,"column":29},"end":{"row":140,"column":30},"action":"remove","lines":["u"]},{"start":{"row":140,"column":28},"end":{"row":140,"column":29},"action":"remove","lines":["b"]},{"start":{"row":140,"column":27},"end":{"row":140,"column":28},"action":"remove","lines":["j"]}],[{"start":{"row":140,"column":27},"end":{"row":140,"column":28},"action":"insert","lines":["m"],"id":88},{"start":{"row":140,"column":28},"end":{"row":140,"column":29},"action":"insert","lines":["a"]},{"start":{"row":140,"column":29},"end":{"row":140,"column":30},"action":"insert","lines":["g"]}],[{"start":{"row":145,"column":69},"end":{"row":146,"column":0},"action":"insert","lines":["",""],"id":89},{"start":{"row":146,"column":0},"end":{"row":147,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":53},"action":"insert","lines":["STATICFILES_STORAGE = 'custom_storages.StaticStorage'"],"id":90}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["#"],"id":91}],[{"start":{"row":153,"column":0},"end":{"row":153,"column":21},"action":"remove","lines":["MEDIA_URL = '/media/'"],"id":92},{"start":{"row":153,"column":0},"end":{"row":153,"column":74},"action":"insert","lines":["MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)"]}],[{"start":{"row":150,"column":31},"end":{"row":151,"column":0},"action":"insert","lines":["",""],"id":93}],[{"start":{"row":151,"column":0},"end":{"row":151,"column":53},"action":"insert","lines":["DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'"],"id":94}],[{"start":{"row":153,"column":23},"end":{"row":154,"column":0},"action":"insert","lines":["",""],"id":95}],[{"start":{"row":154,"column":0},"end":{"row":154,"column":44},"action":"insert","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"],"id":96}],[{"start":{"row":162,"column":0},"end":{"row":162,"column":44},"action":"remove","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"],"id":97}],[{"start":{"row":135,"column":0},"end":{"row":162,"column":0},"action":"remove","lines":["AWS_S3_OBJECT_PARAMETERS = {","    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl':'max-age=94608000',","    ","}","AWS_STORAGE_BUCKET_NAME = 'mag-media'","AWS_S3_REGION_NAME = 'us-east-1'","AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')","AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')","","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'% AWS_STORAGE_BUCKET_NAME","","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","STATICFILES_LOCATION = 'static'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'","MEDIAFILES_LOCATION = 'media'","STATIC_URL = '/static/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')","MESSAGE_STORAGE = \"django.contrib.messages.storage.session.SessionStorage\"","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, \"static\"),",")","",""],"id":98},{"start":{"row":135,"column":0},"end":{"row":156,"column":1},"action":"insert","lines":["AWS_S3_OBJECT_PARAMETERS = {","    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl':'max-age=94608000',","    ","}","AWS_STORAGE_BUCKET_NAME = 'jessbutler-media'","AWS_S3_REGION_NAME = 'us-east-1'","AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')","AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')","","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'% AWS_STORAGE_BUCKET_NAME","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","STATICFILES_LOCATION = 'static'","STATIC_URL = '/static/'","MESSAGE_STORAGE = \"django.contrib.messages.storage.session.SessionStorage\"","MEDIAFILES_LOCATION = 'media'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, \"static\"),",")"]}],[{"start":{"row":140,"column":27},"end":{"row":140,"column":43},"action":"remove","lines":["jessbutler-media"],"id":99},{"start":{"row":140,"column":27},"end":{"row":140,"column":28},"action":"insert","lines":["m"]},{"start":{"row":140,"column":28},"end":{"row":140,"column":29},"action":"insert","lines":["m"]},{"start":{"row":140,"column":29},"end":{"row":140,"column":30},"action":"insert","lines":["a"]},{"start":{"row":140,"column":30},"end":{"row":140,"column":31},"action":"insert","lines":["g"]},{"start":{"row":140,"column":31},"end":{"row":140,"column":32},"action":"insert","lines":["-"]},{"start":{"row":140,"column":32},"end":{"row":140,"column":33},"action":"insert","lines":["m"]},{"start":{"row":140,"column":33},"end":{"row":140,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":140,"column":34},"end":{"row":140,"column":35},"action":"insert","lines":["d"],"id":100},{"start":{"row":140,"column":35},"end":{"row":140,"column":36},"action":"insert","lines":["i"]},{"start":{"row":140,"column":36},"end":{"row":140,"column":37},"action":"insert","lines":["a"]}],[{"start":{"row":140,"column":27},"end":{"row":140,"column":28},"action":"remove","lines":["m"],"id":101}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["£"],"id":102}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["£"],"id":103}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":104}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":1},"end":{"row":13,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1585673263316,"hash":"b58ce8934b5bb33804369e7297846f86bff332bc"}