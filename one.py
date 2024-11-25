"""
这是一个模块
"""
username = input('请输入用户名：')
password = input('请输入密码：')

if username == 'admin' and password == '123456':
    print('登录成功')
else:
    print('登录失败')

total = 0

for i in range(1, 101):
    total += i

print(total)




"""
逻辑运算符练习
"""
from random import randint

def game():
    print('开始改命吧少年')
    money = 1000
    print('你的初始资金是：', money)
    while money > 0:
        go_on = False
        while True:
            bet = int(input('请下注: '))
            if 0 < bet <= money:
                break

        num = randint(1, 6) + randint(1, 6)
        if num == 7 or num == 11:
            print('你赢了')
            money += bet
            print('你的资金是：', money)
        elif num == 2 or num == 3 or num == 12:
            print('你输了')
            money -= bet
            print('你的资金是：', money)
        else:
            go_on = True

        while go_on:
            second = randint(1, 6) + randint(1, 6)
            if second == 7:
                print('你输了')
                money -= bet
                print('你的资金是：', money)
                go_on = False
            elif second == num:
                print('你赢了')
                money += bet
                print('你的资金是：', money)
                go_on = False
            else:
                go_on = True
        if money == 0:
            print('你破产了')
            break

game()
