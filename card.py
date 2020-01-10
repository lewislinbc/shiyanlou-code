import random
card_tuple = ("武则天","嬴政","诸葛亮","宫本武藏","李白")
package = []

while 1:
    a = int(input("充值能让你变得更强\
请选择指令：\
1.抽卡：\
2.查看背包:\
3.整理背包:\
4.离开"))

    if a == 1:
        b = int(input("请输入抽卡次数"))
        for i in range(0,b):
           n = random.randint(0,4)
           print("你抽到了：{}".format(card_tuple[n]))
           package.append(card_tuple[n])

        print("卡已存入背包")
        print("________________________")

    if a == 2:
        if len(package) == 0:
            print('背包暂无英雄，快去抽卡吧')
            print('____________________________')
    else:
        for i in package:
            print(i)
        print("_____________________________________________")

    if a == 3:
        if len(package)==0:
            print('背包暂无英雄，快去抽卡吧')
            print("_________________________________________")
    else:
        package.sort()
        for i in package:
            print(i)
        print("____________________________________")
    if a == 4:
        break

 




