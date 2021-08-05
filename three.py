'''姐就是女王:
随机选择人物： 1、普通没有技能
2、稀有英雄初始值为30。3、传奇英雄不会减少只会增加
需求：
初始值为：10
随机生成三个数字
随机选择一个数字
选择的数字和初始值进行计算（随机加减）
计算过后大于100则任务成功
计算过后小于或等于0则任务失败'''
import random

list1 = ["普通", "稀有", "传奇"]  # ,"稀有","传奇"
# 0     1     2    3 4
#        列表   [                0--------4随机取数字]数字
# print(list1[random.randint(0,len(list1)-1)])
#      列表1    随机数       开始 ，结束（通过这个列表里面有多少元素）
name = list1[random.randint(0, len(list1) - 1)]
print(name)
num = 50
if name == "普通":
    while True:
        i = 0  # 从0开始
        list2 = []
        while i < 3:  # 判断 i是否小于三 i小于三运行下面的代码
            i = i + 1  # 每次循环都加1
            a = random.randint(5, 20)
            list2.append(a)
        # while = 初始值 while判断这个初始值是否大于一个值
        print(list2)
        num1 = list2[random.randint(0, len(list2) - 1)]  # 这是两边随机取出来的数字num1
        print(num1)
        list3 = [1, 2]  # 1 ==加号  2 等于减号
        name2 = list3[random.randint(0, len(list3) - 1)]  # 随机的加减
        if name2 == 1:  # 随机的加减如果等于1 进行加法运算
            num = num1 + num
            print(num)  # 初始num 加上一个随机取出来的数字
        elif name2 == 2:  # 随机的加减如果等于1 进行减法运算
            num = num1 - num
            print(num)  # 初始num 加上一个随机取出来的数字
        if num > 100:
            print("任务成功你的分数为", num)
            break
        elif num <= 0:
            print("任务失败你的分数为", num)
            break
if name == "稀有":
    while True:
        i = 0  # 从0开始
        list2 = []
        while i < 3:  # 判断 i是否小于三 i小于三运行下面的代码
            i = i + 1  # 每次循环都加1
            a = random.randint(5, 20)
            list2.append(a)
        # while = 初始值 while判断这个初始值是否大于一个值
        print(list2)
        num1 = list2[random.randint(0, len(list2) - 1)]  # 这是两边随机取出来的数字num1
        print(num1)
        list3 = [1, 2]  # 1 ==加号  2 等于减号
        name2 = list3[random.randint(0, len(list3) - 1)]  # 随机的加减
        if name2 == 1:  # 随机的加减如果等于1 进行加法运算
            num = num1 + num
            print(num)  # 初始num 加上一个随机取出来的数字
        elif name2 == 2:  # 随机的加减如果等于1 进行减法运算
            num = num1 - num
            print(num)  # 初始num 加上一个随机取出来的数字
        if num > 100:
            print("任务成功你的分数为", num)
            break
        elif num <= 0:
            print("任务失败你的分数为", num)
            break
if name == "传奇":
    while True:
        i = 0  # 从0开始
        list2 = []
        while i < 3:  # 判断 i是否小于三 i小于三运行下面的代码
            i = i + 1  # 每次循环都加1
            a = random.randint(5, 20)
            list2.append(a)
        # while = 初始值 while判断这个初始值是否大于一个值
        print(list2)
        num1 = list2[random.randint(0, len(list2) - 1)]  # 这是两边随机取出来的数字num1
        print(num1)
        list3 = [1, 2]  # 1 ==加号  2 等于减号
        name2 = list3[random.randint(0, len(list3) - 1)]  # 随机的加减
        if name2 == 1:  # 随机的加减如果等于1 进行加法运算
            num = num1 + num
            print(num)  # 初始num 加上一个随机取出来的数字
        elif name2 == 2:  # 随机的加减如果等于1 进行减法运算
            num = num1 - num
            print(num)  # 初始num 加上一个随机取出来的数字
        if num > 100:
            print("任务成功你的分数为", num)
            break
        elif num <= 0:
            print("任务失败你的分数为", num)
            break
