
# 移动列表元素
unconfirmed_user = ["JavaScript","Python","Ruby","PHP"]
confirmed_user   = []

#循环添加
while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    confirmed_user.append(current_user)

print(confirmed_user)