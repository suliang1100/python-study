
# 定义可供调用的模块

#传递任意数量的关键字实参
def greeter_lan(first,last,**languages):
    """双星号创建空字典"""
    profile = {}
    profile["first"] = first
    profile["last"] = last
    for k,v in languages.items():
        profile[k] = v
    print(profile)