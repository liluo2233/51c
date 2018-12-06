#!/usr/bin/env/Python
# ----coding: utf-8 ------
# unit conversion.py
# author:wangchen

'''

51memo.py
1.需要一个菜单，供用户选择
2.判断用户选择哪个
3.继续判断
4.输出结果。

'''
print('欢迎使用万能转换器'.center(30,'-'))
menu = {
    'T':'温度',
    'L':'长度',
    'C':'货币'
}


choose = ''
while choose != 'q':
    for k,v in menu.items():
        print(k,v)
    temp = input('请选择转换类型：')

    if temp == 'T':
        t = input('请输入温度（示例：1C或1F）')
        if t.endswith('C'):
            t = float(t.strip('C'))
            # 摄氏温度转华氏温度： Tf = （9/5）Tc + 32
            print(f'摄氏温度：{t}度 = 华氏温度： {(9/5) * t + 32}度')
        else:
            t = float(t.strip('F'))
            # 华氏温度换摄氏温度： Tc = （5/9））（Tf-32）
            print(f'华氏温度：{t}度 = 摄氏温度：{(5/9) * (t - 32)}度')
    #长度单位：厘米cm 米m
    elif temp == 'L':
        l = input('请输入长度（示例：1mi或1km）：')
        if l.endswith('mi'):
            l = float(l.strip('mi'))
            # 1mi（英里） = 1.6km（千米）
            print(f'{l}mi = {l*1.61}m')
        else: 
            l = float(l.strip('km'))
            print(f'{l}m = {l/1.61}cm')
    # 货币单位：美元USD 人民币 RMB
    else:
        c = input('请输入货币（示例：1USD或1RMB）：')
        if c.endswith('USD') :
            c = float(c.strip('USD'))
            # 1 USD = 6.9429 RMB
            print(f'{c} USD = {c * 6.9} RMB')
        else:
            # 1 RMB = 0.144 USD
            c = float(c.strip('RMB'))
            print(f'{c} RMB = {c * 0.14} USD')
            
    choose = input('按任意键返回，退出请按q')