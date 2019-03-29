import random
secert = random.randint(1,100)
times = 3

while times:
    num = input("输入")
    if num.isdigit():
        tmp = int(num)
        if tmp == secert:
            print("对")
            break
        elif tmp < secert:
            print("小了")
            times = times - 1
        else:
            print("大了")
            times = times - 1
    else:
        print("请输入数字！")
print("机会用完了")