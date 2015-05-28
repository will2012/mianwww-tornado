# -*- coding: utf-8 -*-
from webservice.handlers import *
urls = [(r'/v1/categories', CategoryListHandler),
        (r'/v1/posts/([0-9]+)/([0-9]+)', PostListlHandler)]
