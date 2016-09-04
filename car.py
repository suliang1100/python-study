
# 类的继承

#定义父类
class Car():

    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("这辆车的行驶里程累计：" + self.odometer_reading + "米")

    #更新行驶里程
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("不能回拨里程")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

#定义子类
class EletricCar(Car):

    """定义电动车的不同之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery_size = 70

    #描述电瓶信息
    def descript_battery(self):
        print("这辆车拥有一个"+str(self.battery_size)+"kw/h的电池")

    #计算续航里程
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "这辆车的续航里程为：" + str(range) + "公里"
        print(message)

my_tesla = EletricCar("Tesla","model s",2016)
print(my_tesla.descriptive_name())
my_tesla.descript_battery()
my_tesla.get_range()