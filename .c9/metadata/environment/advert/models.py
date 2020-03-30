{"filter":false,"title":"models.py","tooltip":"/advert/models.py","undoManager":{"mark":50,"position":50,"stack":[[{"start":{"row":9,"column":28},"end":{"row":9,"column":38},"action":"insert","lines":["default=''"],"id":81}],[{"start":{"row":5,"column":63},"end":{"row":5,"column":64},"action":"insert","lines":[","],"id":82}],[{"start":{"row":5,"column":64},"end":{"row":5,"column":65},"action":"insert","lines":[" "],"id":83}],[{"start":{"row":5,"column":65},"end":{"row":5,"column":79},"action":"insert","lines":["required=False"],"id":84}],[{"start":{"row":6,"column":69},"end":{"row":6,"column":70},"action":"insert","lines":[","],"id":85}],[{"start":{"row":6,"column":70},"end":{"row":6,"column":71},"action":"insert","lines":[" "],"id":86}],[{"start":{"row":6,"column":71},"end":{"row":6,"column":85},"action":"insert","lines":["required=False"],"id":87}],[{"start":{"row":7,"column":61},"end":{"row":7,"column":62},"action":"insert","lines":[","],"id":88}],[{"start":{"row":7,"column":62},"end":{"row":7,"column":63},"action":"insert","lines":[" "],"id":89},{"start":{"row":7,"column":63},"end":{"row":7,"column":64},"action":"insert","lines":["v"]}],[{"start":{"row":7,"column":63},"end":{"row":7,"column":64},"action":"remove","lines":["v"],"id":90}],[{"start":{"row":7,"column":63},"end":{"row":7,"column":77},"action":"insert","lines":["required=False"],"id":91}],[{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":[","],"id":92}],[{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":[" "],"id":93}],[{"start":{"row":8,"column":63},"end":{"row":8,"column":77},"action":"insert","lines":["required=False"],"id":94}],[{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":[","],"id":95}],[{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":[" "],"id":96}],[{"start":{"row":9,"column":40},"end":{"row":9,"column":54},"action":"insert","lines":["required=False"],"id":97}],[{"start":{"row":10,"column":38},"end":{"row":10,"column":52},"action":"insert","lines":["required=False"],"id":98}],[{"start":{"row":11,"column":44},"end":{"row":11,"column":58},"action":"insert","lines":["required=False"],"id":99}],[{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":[","],"id":100}],[{"start":{"row":12,"column":42},"end":{"row":12,"column":56},"action":"insert","lines":["required=False"],"id":101}],[{"start":{"row":5,"column":65},"end":{"row":5,"column":79},"action":"remove","lines":["required=False"],"id":102}],[{"start":{"row":6,"column":71},"end":{"row":6,"column":85},"action":"remove","lines":["required=False"],"id":103}],[{"start":{"row":7,"column":61},"end":{"row":7,"column":77},"action":"remove","lines":[", required=False"],"id":104}],[{"start":{"row":5,"column":64},"end":{"row":5,"column":65},"action":"remove","lines":[" "],"id":105},{"start":{"row":5,"column":63},"end":{"row":5,"column":64},"action":"remove","lines":[","]}],[{"start":{"row":8,"column":61},"end":{"row":8,"column":77},"action":"remove","lines":[", required=False"],"id":106}],[{"start":{"row":9,"column":38},"end":{"row":9,"column":54},"action":"remove","lines":[", required=False"],"id":107}],[{"start":{"row":10,"column":38},"end":{"row":10,"column":52},"action":"remove","lines":["required=False"],"id":108}],[{"start":{"row":11,"column":44},"end":{"row":11,"column":58},"action":"remove","lines":["required=False"],"id":110}],[{"start":{"row":12,"column":42},"end":{"row":12,"column":56},"action":"remove","lines":["required=False"],"id":111},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"remove","lines":[","]}],[{"start":{"row":6,"column":4},"end":{"row":14,"column":0},"action":"remove","lines":["user = models.ForeignKey(User, null=True,on_delete=models.CASCADE, )","    advert_image = models.ImageField(upload_to='media/images')","    header_image = models.ImageField(upload_to='media/images')","    info = models.TextField(default='')","    contact_email = models.EmailField()","    contact_telephone = models.IntegerField()","    slug = models.SlugField(max_length=50)","    category = models.CharField(max_length=254, default='')",""],"id":112}],[{"start":{"row":5,"column":64},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":113},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":8,"column":45},"action":"insert","lines":["info = models.TextField(default='')","    contact_email = models.EmailField()","    contact_telephone = models.IntegerField()"],"id":114}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":45},"action":"remove","lines":["models.IntegerField()"],"id":115},{"start":{"row":8,"column":24},"end":{"row":8,"column":68},"action":"insert","lines":["models.CharField(max_length=254, default='')"]}],[{"start":{"row":8,"column":68},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":116},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":72},"action":"insert","lines":["user = models.ForeignKey(User, null=True,on_delete=models.CASCADE, )"],"id":117}],[{"start":{"row":9,"column":69},"end":{"row":9,"column":70},"action":"remove","lines":[","],"id":118}],[{"start":{"row":9,"column":71},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":119},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":11,"column":59},"action":"insert","lines":["  slug = models.SlugField(max_length=50)","    category = models.CharField(max_length=254, default='')"],"id":120}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"remove","lines":[" "],"id":121},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":11,"column":59},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":122},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":62},"action":"insert","lines":["advert_image = models.ImageField(upload_to='media/images')"],"id":123}],[{"start":{"row":12,"column":62},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":124},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":63},"action":"insert","lines":[" header_image = models.ImageField(upload_to='media/images')"],"id":125}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":[" "],"id":126}],[{"start":{"row":12,"column":54},"end":{"row":12,"column":60},"action":"remove","lines":["images"],"id":127},{"start":{"row":12,"column":54},"end":{"row":12,"column":55},"action":"insert","lines":["a"]},{"start":{"row":12,"column":55},"end":{"row":12,"column":56},"action":"insert","lines":["d"]},{"start":{"row":12,"column":56},"end":{"row":12,"column":57},"action":"insert","lines":["v"]},{"start":{"row":12,"column":57},"end":{"row":12,"column":58},"action":"insert","lines":["e"]},{"start":{"row":12,"column":58},"end":{"row":12,"column":59},"action":"insert","lines":["r"]},{"start":{"row":12,"column":59},"end":{"row":12,"column":60},"action":"insert","lines":["t"]},{"start":{"row":12,"column":60},"end":{"row":12,"column":61},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":62},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":129},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["w"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["e"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["b"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["i"],"id":130},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["t"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":[" "],"id":131},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":[" "],"id":132}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":58},"action":"insert","lines":["models.CharField(max_length=254, default='')"],"id":133}]]},"ace":{"folds":[],"scrolltop":21,"scrollleft":0,"selection":{"start":{"row":14,"column":58},"end":{"row":14,"column":58},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1585582312086,"hash":"66e14b7c361ac837d7c7a91f24550f34bbded9cc"}