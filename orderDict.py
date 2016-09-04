
# 使用标准库方法
# 创建有序的字典
from collections import OrderedDict

languages = OrderedDict()
#languages = {}

languages["suliang"] = "Python"
languages["zhoujielun"] = "JavaScript"
languages["wanglihong"] = "Ruby"
languages["linjunjie"] = "PHP"

for name,language in languages.items():
    print(name.title()+"最爱的编程语言是:" +language.title())


#随机产生骰子点数
from random import randint

class Die():

    #初始化点数为6
    def __init__(self,times=10):
        self.sides = 6
        self.times = times

    #随机产生一个点数
    def roll_die(self):

        #循环打印
        for value in range(0,self.times):
            self.sides = randint(1, 6)
            print(self.sides)
        print("----")

my_die1 = Die()
my_die2 = Die(20)
my_die1.roll_die()
my_die2.roll_die()