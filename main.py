import tornado.ioloop
import tornado.web
import os
from views.json.json_views import JsonHandle
from views.web.web_views import WebHandle
from url_router import url_wrapper, include


class Application(tornado.web.Application):
    def __init__(self):
        # handlers = [
        #     (r"/web/", WebHandle),
        #     (r"/json/", JsonHandle),
        # ]
        handlers = url_wrapper([
            (r'/json/', include('views.json.json_urls')),
            (r'/web/', include('views.web.web_urls'))
        ])

        # 定義tornado服務器的配置項，如static/templates目錄位置，debug級別等
        # settings = dict(
        #     debug=True,
        #     static_path=os.path.join(os.path.dirname(__file__), "static"),
        #     template_path=os.path.join(os.path.dirname(__file__), "templates")
        # )
        #tornado.web.Application.__init__(self, handlers, **settings)
        tornado.web.Application.__init__(self, handlers)


if __name__ == '__main__':
    print('Server is running')
    Application().listen(8888, xheaders=True)
    tornado.ioloop.IOLoop.current().start()
