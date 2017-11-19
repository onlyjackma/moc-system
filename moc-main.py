# -*- coding:utf-8 -*-
import os
import tornado.ioloop
import tornado.web
import time
from person_edit import PersonEditHandler

class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome to moc-system")
    def post(self, *args, **kwargs):
        return

handlers = [
    (r'/',MainPageHandler),
    (r'/person_edit',PersonEditHandler),

]

settings = {
    'static_path':os.path.join(os.path.dirname(__file__),'static'),
    'template_path':os.path.join(os.path.dirname(__file__),'templates')
    }


def MOC_main():
    print("Startting the moc system!!!")
    app = tornado.web.Application(handlers,**settings)
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    MOC_main()