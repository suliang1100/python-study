
# 操作字典列表

#创建包含30个外星人的字典列表
aliens = []
for alien_number in range(30):
    new_alien = {
        "color":"green",
        "points":5,
        "speed":"slow"
    }
    aliens.append(new_alien)

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少外星人
print("外星人总数为:"+str(len(aliens)))

#修改前3个外星人
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = 10
        alien["points"] = "medium"
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

print(aliens)