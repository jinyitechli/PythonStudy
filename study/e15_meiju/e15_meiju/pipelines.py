# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
class E15MeijuPipeline(object):
    def process_item(self, item, spider):
        return item

class MeijuPipeline(object):

    def  __init__(self):
        print('init...meiju')
        self.file = codecs.open('meiju.json','wb',encoding='utf-8')



    def process_item(self,item,spider):
        f = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(f)
        return item
