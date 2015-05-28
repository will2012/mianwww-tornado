# -*- coding: utf-8 -*-
import json
from operator import attrgetter

from webservice.base import APIHandler
from config import SETTINGS
import MySQLdb
class CategoryListHandler(APIHandler):
    def get(self):
        categories = []
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='AAAaaa111',db='mian',port=3306,charset='utf8')
            cur=conn.cursor()
            cur.execute('select id, category_name from mian_category')
            for row in cur.fetchall():
                item = {}
                item['id'] = row[0]
                item['name'] = row[1]
                categories.append(item)
            cur.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        self.finish(json.dumps(categories, ensure_ascii=False))

class PostslHandler(APIHandler):
     def get(self, category_id, page):
         posts = []
         try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='AAAaaa111',db='mian',port=3306,charset='utf8')
            cur=conn.cursor()
            begin = int(page) * 20
            end = (int(page) + 1) * 20
            sql = 'select post_title,post_content from mian_post where category_id=%s  limit %s,%s'
            #print begin
            #print end
            #print sql
            values=[category_id, begin, end]
            cur.execute(sql, values)
            for row in cur.fetchall():
                item = {}
                item['title'] = row[0]
                item['post_content'] = row[1]
                posts.append(item)
            cur.close()
            conn.close()
         except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
         self.finish(json.dumps(posts, ensure_ascii=False))

