from google.appengine.ext import db

# Create your models here.


class Greeting(db.Model):
    author = db.UserProperty()
    content = db.TextProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class Scumbag(db.Model):
    content = db.TextProperty()