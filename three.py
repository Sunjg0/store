'''
 1、随机点名
 2、随机生成棒棒糖
容器类型：
    int、str、double boolean
     元组：()------tuple 不可修改
     列表[]: 可以修改的
     字典{ ""   :  "",}键值对的关系
            键      值
            通过调用键来获取值
    姐就是女王 :
    选择人物： 1、普通  2、初始3个   3、不会减少
    需求：
    第一步：初始值：1 ：赢：20 输：0
    进行计算 : 随机三个数字（1,7）

'''

#增加一个代码判断之后结束   break#跳出循环
import random  #生成随机数的模块
name = ["王佳琪", "牛埔至", "王天旭", "小宝", "陆经理"]   #是个列表   内容是个范围
i = 0 #的初始值为0
print("第一个",i)
while i<10: #进行判断：当i<2时运行下面的代码
    i+=1   #i  = i +1   结束整个循环  i=>结束
    chose=input("请输入您的业务（1、点名2、分发棒棒糖）") #从键盘上获取的是str 赋值为chose
    print("第二个",i)
    if chose == "1":   #一个等于号是赋值  两个是判断  chose ==1  运行下面的代码 如果chose不等于1 跳过
        a=len(name)   #a获取到的数字 0 1 2 3 4
        index=random.randint(0,a-1)  #随机生成的角标 a:int,B:int
        print(name[index])
    elif chose =="2":  #如果第一个判断跳过 执行第二个判断 chose==2 如果是运行下面的代码 如不等于2 跳过
        num=random.randint(5,10)
        print("获得了",num,"个棒棒糖")
    else: #如果第二个判断跳过 直接执行下面的代码
        print("你错了")
print(name[index],"获得了",num,"个棒棒糖")
