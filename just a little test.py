# -*- coding: utf-8 -*-
# 2016/7/6 8:59
"""
-------------------------------------------------------------------------------
Function:   just a little test
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
pic="""
_                                             _
| |                                           | |
| |__   ___  _ __ ___   _____      _____  _ __| | __
| '_ \ / _ \| '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| | | | (_) | | | | | |  __/\ V  V / (_) | |  |   <
|_| |_|\___/|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
"""
print pic
#4.查找字符串
s=raw_input("请输入一个子字符串:")
arr_s=[x for x in s]
#将输入的字符串列表化，方便操作
t=raw_input("请再输入一个父字符串:")
arr_t=[x for x in t]

def check(keyword,cut_arr):
    if keyword in arr_t[cut_arr:]:
        return True
    else:
        return False
cut=0
flag=True
connect_str=''
for test_box in arr_s :
    if flag:
        print "开始测试%s是否在%s中"%(test_box,s[cut:]) #这里是核心，利用数组切片
        flag=check(test_box,cut)
        cut=arr_s.index(test_box)
        connect_str=connect_str+test_box
        print(connect_str)
    else:
        break
if connect_str==s:                         #检查当所有的字符串都相匹配后说明是其子字符串
    print"%s是%s的子字符串"%(s,t)
    print"YES"
else:
    print"NO"                             #之所以有很多注释是为了方便你理解我算法的思路

#3.第三题
six_raw=raw_input("请输入一个六进制数字")
six_int=abs(int(six_raw))
ten=0
count=1
for i in str(six_raw):
    if int(i)<6:
       ten=ten+int(i)*(pow(len(six_raw)-count,6))
       count=count+1
    else:
        print "fuck you "
        ten='error,can not print out'
        break
print ten

#2.第二题
a=1
b=2
i=0
sum=0
while i<20:
    sum=sum+b/a
    a=b
    b=a+b
    i=i+1
print sum
#1.第一题
raw_num=raw_input('随便输入一个数字:')
print(len(raw_num))
print(raw_num[::-1])


