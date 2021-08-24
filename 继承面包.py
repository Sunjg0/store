from threading import Thread
import time


class mianbao(Thread):
    chushi = ''
    goods = 0  # 篮子面包个数，
    mon = 3000  # 客户金额

    def run(self) -> None:
        while True:
            self.goods+=1
            self.mon-=3
            print(self.chushi,self.goods,'个面包')
            if self.goods == 500:
                print(self.goods,'个面包篮子已经满了，请稍等两秒')
                time.sleep(2)
            if self.mon == 0:
                print('面包卖没了')
                break





p1 = mianbao()
p1.chushi = '孙子杰'
p1.start()
p2 = mianbao()
p2.chushi = '孙建国'
p2.start()
p3 = mianbao()
p3.chushi = '孙道然'
p3.start()


