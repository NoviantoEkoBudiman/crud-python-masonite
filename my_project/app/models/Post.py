""" Post Model """

from masoniteorm.models import Model


class Post(Model):
    __database__ = 'posts'
    __fillable__ = ['id','title','author_id','body']