
# 定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello world")

greet_user()

#传递参数
def greet_argument(username):
    """传递参数给函数"""
    print("Your name is:"+username)

greet_argument("suliang")

#使用关键字实参
def greeter(username,age):
    """传递关键字实参"""
    print("Your name is:"+username+",age:"+age)

greeter(age="26",username="suliang")

#使用可选参数
def greeter_user(first_name,last_name,middle_name=""):
    """使用关键字传参的方式来使用可选参数"""
    if middle_name:
        fullname = first_name+" "+middle_name+" "+last_name
    else:
        fullname = first_name+" "+last_name
    return fullname.title()

person1 = greeter_user("zhou","lun","jie")
person2 = greeter_user("su","liang")

print(person1)
print(person2)

#传递任意数量的实参
def greeter_args(*languages):
    """将全部参数封装到一个元组中去"""
    print(languages)

greeter_args("JavaScript")
greeter_args("JavaScript","Python","Ruby")

#传递任意数量的关键字实参
def greeter_lan(first,last,**languages):
    """双星号创建空字典"""
    profile = {}
    profile["first"] = first
    profile["last"] = last
    for k,v in languages.items():
        profile[k] = v
    print(profile)

greeter_lan("su","liang",location="hangzhou")
greeter_lan("su","liang",location="hangzhou",age="26")