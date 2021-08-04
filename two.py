import random
import time
i = 0
for i in range(10):
    num = random.randint(0, 9)
    a = int(input("请输入0到9之间的实数"))
    if num == a:
        print("输入正确")
    elif num < a < num:
        print("输入实数超过范围，请5秒后输入"),time.sleep(5)
    else:print("输入不正确")
    i +=1
