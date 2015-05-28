# -*- coding: utf-8 -*-
import json
from operator import attrgetter

from webservice.base import APIHandler
from config import SETTINGS

class CategoryListHandler(APIHandler):
    def get(self):
        self.finish('Category List')



class PostListlHandler(APIHandler):
     def get(self):
        self.finish('PostHandler')


