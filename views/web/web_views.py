import tornado.web


class WebHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("web view")
