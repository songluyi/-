# -*- coding: utf-8 -*-
# 2016/9/18 14:07
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import os
query_string=raw_input('请输入要查询的关键词：')
down_dir = unicode(query_string,'utf-8')
print(down_dir)
os.makedirs(down_dir)
# query_string=u"家具"
# os.makedirs(query_string)
