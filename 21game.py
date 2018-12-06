#!/usr/bin/env/Python
# ----coding: utf-8 ------
# 21game.py

import random

'''
1.两个玩家，游戏开始先输入名字
2.用字典保存信息：姓名，获胜次数
3.电脑随机产生2个数，每个玩家轮流猜1个数，与电脑随机俩那个歌数求和，接近21的胜
4.每轮结束显示玩家信息
5. 按q退出游戏

'''


targat = 21
print('欢迎来到21点游戏'.center(30,'-'))
# 创建用户 用字典保存玩家信息
player_1 = input('输入玩家1姓名:')
player_2 = input('输入玩家2姓名:')
print(f'玩家1：{player_1}, 玩家2：{player_2}')

player_dict = {
    'player_1':{'win':0},
    'player_2':{'win':0}
}

choose = input(f'请输入任意键开始游戏')
n = 0
count1 = 0
count2 = 0
while choose != 'q':
    n += 1
    num_1 = random.randint(1,10)
    num_2 = random.randint(1,10)
    player_1_guess = input('请玩家1输入一个1-10之间的整数：')
    player_2_guess = input('请玩家2输入一个1-10之间的整数：')
    sum1 = num_1+ num_2+ int(player_1_guess)
    sum2 = num_1+ num_2+ int(player_2_guess)

    if abs(sum1-targat)>abs(sum2-targat): 
        count1 += 1
        player_dict['player_1']['win'] += count1 
        print(f'{player_1}的点数为：{sum1}   {player_2}的点数为：{sum2}')
        print(f'{player_2}获胜！')
    else :
        count2 += 1
        player_dict['player_2']['win'] += count2
        print(f'{player_1}的点数为：{sum1}   {player_2}的点数为：{sum2}')
        print(f'{player_1}获胜！')
    print(f'共进行了{n}轮游戏，{player_1}赢了{count1}次，{player_2}赢了{count2}')
    choose = input(f'按任意键继续游戏，退出请按q')
else:
    print('游戏结束，再见')