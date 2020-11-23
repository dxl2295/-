"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：邓小龙
日期：2020.11.23
"""
import random


def name_to_number(name):#将四个选择分别对应为四个数
    if name == '石头':
        return 0
    elif name == '史波克':
        return 1
    elif name == '布':
        return 2
    elif name == '蜥蜴':
        return 3
    elif name == '剪刀':
        return 4
    else:
        print('请从石头，史波克，布，蜥蜴，剪刀 中任选一个')


def number_to_name(number):
    if number in range(0, 5):
        if number == 0:
            return '石头'
        elif number == 1:
            return '史波克'
        elif number == 2:
            return '布'
        elif number == 3:
            return '蜥蜴'
        elif number == 4:
            return '剪刀'
    else:
        print('请在0-4中任意选一个数')


def rpsls(player_choice):#游戏规则的设定
    print()
    print('玩家选择了', player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print('电脑选择了', comp_choice)
    if player_number - comp_number in range(-4, -2) or range(1, 3):
        print('玩家赢了!')
    elif player_number - comp_number in range(-2, 0) or range(3, 5):
        print('机器赢了!')
    elif player_number - comp_number == 0:
        print('平局!')
    else:
        print('Error: No Correct Name!')


print('"Rock-paper-scissors-lizard-Spock" 游戏开始')
rpsls("石头")
rpsls("史波克")
rpsls("布")
rpsls("蜥蜴")
rpsls("剪刀")

