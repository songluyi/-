# -*- coding: utf-8 -*-
# 2016/6/23 21:45
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
world=[x for x in range(1,20)]
full_world=world+world[::-1][1:19]
print(len(full_world))
print(full_world)
print(full_world[7])
print 7%35
print full_world[7-1]