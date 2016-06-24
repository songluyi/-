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
def save_file(result):
        f=open('stu_number.txt','a')
        f.write(result)
        f.close()
def plus(place):
    place=place+1
    return place
f=open('in.txt')
readline=f.readlines()
N=int(readline[0])
data_1=readline[1].split(' ')
data_2=readline[2].split(' ')
name_a,place_a,neili_a,wuyi_a,health_a=data_1
health_a=health_a.strip('\n')
name_b,place_b,neili_b,wuyi_b,health_b=data_2
print place_b
world=[x for x in range(1,20)]
full_world=world+world[::-1][1:19]
print full_world
count,block_a,block_b=1,1,1
while count<=N :
    place_a=(int(place_a)%36)
    place_b=(int(place_b)%36)
    print count
    # if place_b==0:
    #     place_b=place_b+2
    if full_world[place_a-1]==full_world[place_b-1] and health_a>0 and health_b>0:
        print'they are having a fight at %d place for the %d'%(full_world[place_b-1],count)
        ATK_a=int((0.5*int(neili_a)+0.5*int(wuyi_a))*(int(health_a)+10)/100)
        ATK_b=int((0.2*int(neili_b)+0.8*int(wuyi_b))*(int(health_b)+10)/100)
        health_a=int(health_a)-ATK_b
        health_b=int(health_b)-ATK_a
        if health_a <= 0:
            block_a=-1
            result=name_a+' '+str(full_world[place_a-1])+' '+str(health_a)
            save_file(result)
        elif health_b<=0:
            block_b=-1
            result=name_b+' '+str(full_world[place_b-1])+' '+str(health_b)
            save_file(result)
    if health_a>0:
        place_a=int(place_a)+1
    if health_b>0:
        place_b=int(place_b)+2
    count=count+1

if cmp(health_a,health_b)>0:
        result='\n'+name_a+' '+str(full_world[place_a-1])+' '+str(health_a)
        save_file(result)
elif cmp(health_a,health_b)<0:
        result='\n'+name_b+' '+str(full_world[place_b-1])+' '+str(health_b)
        save_file(result)








