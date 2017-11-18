import tornado.web
class EditHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("edit.html")
    def post(self, *args, **kwargs):
        return
