import time

class strtime():
    def __init__(self):
        self.unit=['年','月','天','小时','分钟','秒']
        self.prompt='计时未开始哦'
        self.lasted=[]
        self.begin=0
        self.over=0

    def __str__(self):
        return self.prompt

    __repr__=__str__

    def __add__(self, other):
        prompt="总共运行了"
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return  prompt

    def star(self):
        self.begin=time.localtime()
        print("记时开始！")

    def stop(self):
        self.over=time.localtime()
        self._cal()
        print("记时结束！")

    def _cal(self):
        self.lasted = []
        self.prompt='总共运行了'
        for index in range(6):
            self.lasted.append(self.over[index]-self.begin[index])
            if self.lasted[index]:
                 self.prompt+=str(self.lasted[index])+self.unit[index]

t=strtime()
t.star()
time.sleep(10)
t.stop()
print(t)
t1=strtime()
t1.star()
time.sleep(10)
t1.stop()
print(t1)
print(t+t1)



