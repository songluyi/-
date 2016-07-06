# -*- coding: utf-8 -*-
# 2016/6/23 17:52
"""
-------------------------------------------------------------------------------
Function:   A little game about Martial arts
Version:    1.0
Author:     anonymous
Contact:    anonymous
 
-------------------------------------------------------------------------------
"""
def save_file(result):                        #需要保存的地方有点多，写个函数调用
        f=open('stu_number.txt','a')       #这里使用追加的方式打开
        f.write(result)
        f.close()
#下面开始从txt文本读入三行数据
f=open('in.txt')
readline=f.readlines()
N=int(readline[0])                        #注意，请不要修改in.txt文件中第一行的值小于40我默认为50，四十的算法是有问题的。
data_1=readline[1].split(' ')            #用内置函数做一个字符串的切割
data_2=readline[2].split(' ')
name_a,place_a,neili_a,wuyi_a,health_a=data_1
health_a=health_a.strip('\n')           #注意，这里在读入的时候需要把换行符给剔除掉，使用python内置strip函数即可
name_b,place_b,neili_b,wuyi_b,health_b=data_2
#将武侠世界的单元格列表化，将一去一回作为一个整体命名为新的full——world变量
world=[x for x in range(1,20)]
full_world=world+world[::-1][1:18]  #去除19和1这些多余的两个，这个列表类似为【1,2.......，17,18,19,18，.....，2】
print full_world
count,block_a,block_b=1,1,1        #这里count作为计数器用来控制下文的while循环，block作为锁，用来判定大侠是否死亡的一把锁
while count<=N :
    place_a=(int(place_a)%36)     #每三十六次就会循环
    place_b=(int(place_b)%36)
    print count
    # if place_b==0:
    #     place_b=place_b+2          #这个是算法判定，用来剔除18 和 2的
    if full_world[place_a-1]==full_world[place_b-1] and health_a>0 and health_b>0:                 #判断战斗是否开始
        print'they are having a fight at %d place for the %d'%(full_world[place_b-1],count) #开始就说明在哪个格子第几次循环发生的
        ATK_a=int((0.5*int(neili_a)+0.5*int(wuyi_a))*(int(health_a)+10)/100)
        ATK_b=int((0.2*int(neili_b)+0.8*int(wuyi_b))*(int(health_b)+10)/100)
        health_a=int(health_a)-ATK_b
        health_b=int(health_b)-ATK_a
        if health_a <= 0:            #如果生命值小于零，加一把锁，使他不可以参与战斗或者单元格的移动
            block_a=-1

        elif health_b<=0:
            block_b=-1

    if health_a>0:                   #判定只有生命值0才可以在单元格走动
        place_a=int(place_a)+1
    if health_b>0:
        place_b=int(place_b)+2
    count=count+1
#记录大侠
result='\n'+name_a+' '+str(full_world[place_a-1])+' '+str(health_a)
save_file(result)
result='\n'+name_b+' '+str(full_world[place_b-1])+' '+str(health_b)
save_file(result)