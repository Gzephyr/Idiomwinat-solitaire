# -*- coding: utf-8 -*-
"""
Created on Sun Jun 6 20:53:16 2021

@author: 86181
"""

import random
import copy

all_idiom = []
rand_all_idiom = []
memory = set()  # 记忆集合，用于判断成语是否被重复使用
#set()函数创建一个无序不重复元素集，进行关系测试，删除重复数据

#将成语数据集读入
def readall():
    global all_idiom, rand_all_idiom
    with open('idiom.txt', 'r',encoding = 'utf-8') as f:
        all_idiom = f.readlines()
    rand_all_idiom = copy.deepcopy(all_idiom) #深拷贝，对象不受原对象变化影响
    #rand_all_idiom = copy.copy(all_idiom) 
 
#判断是否为成语,该成语是否在数据集中
def idiom_exists(x):
    x = x.strip()  #删除whitespace
    #strip()只能删除开头和结尾的字符，中间不可以
    for i in set(all_idiom):#遍历set与list类似，都可通过for循环实现
        if x == i.strip():
            return True
    return False

 #判断两个成语是否可以接龙（首尾字母和四字）
def idiom_test(idiom1, idiom2):
    idiom1 = idiom1.strip()
    idiom2 = idiom2.strip()
    if idiom2[0] != idiom1[-1] or len(idiom2) < 4:
        return False
    return True

#实现接龙，NPC随机挑选一个成语开始
def idiom_select(x):
    if not x: 
    #if x is not none
   #none同false，即x为合格的成语时
        i = random.choice(all_idiom) #choice() 方法返回一个列表，元组或字符串的随机项
#choice()不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法
        i = i.strip()
        return i #返回该成语的接龙匹配成语
    else:
        #random(rand_all_idiom)
        random.shuffle(rand_all_idiom)   #shuffle() 方法将序列的所有元素随机排序。
        x = x.strip()
        for i in rand_all_idiom:
            i = i.strip()
            if i[0] != x[-1] or len(i) < 4:
                continue
            return i
        return None


def pc_answer(t):
    cycle_flag = 0
    while True:  # 玩家答不上，电脑尝试思考答案
        p = idiom_select(t)

        cycle_flag += 1
        if p not in memory:
            break
        if cycle_flag > 5:
            p = ''
            break
    return p



def pc_question():
    while True:
        t = idiom_select(None)
        if not t in memory:
            break
    if t:
        memory.add(t)
    return t
