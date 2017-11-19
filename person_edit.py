# -*- coding:utf-8 -*-
import tornado.web
import os
class PersonEditHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("person_edit.html")
    def post(self, *args, **kwargs):
        upload_img=os.path.join(os.path.dirname(__file__),'static/images')
        if not os.path.exists(upload_img) :
            os.makedirs(upload_img)
        moc_name = self.get_body_argument('moc-name')
        moc_part = self.get_body_argument('moc-part')
        moc_depart = self.get_body_argument('moc-depart')

        print(moc_name,moc_part,moc_depart)
        try:
            himgs = self.request.files['moc-himg']
            print(len(himgs))
            for himg in himgs:

                for x in himg:
                    print(x)
                file_name = himg['filename']
                print(file_name)
                filepath = os.path.join(upload_img, file_name)
                print(filepath)
                with open(filepath, 'wb') as imgp:
                    imgp.write(himg['body'])
        except KeyError,e:
            print(e.message)
            self.write("there is no image")

        self.write(moc_name+moc_part+moc_depart)

        return
