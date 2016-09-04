
#使用类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age  = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title()+" is sitting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title()+" rolled over!")

#根据类创建实例
my_dog = Dog("wangcai",5)
my_dog.sit()
my_dog.roll_over()