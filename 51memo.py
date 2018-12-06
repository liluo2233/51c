#!/usr/bin/env/Python
# ----coding: utf-8 ------
# 51memo.py
# test
# author: wangchen

from color_me import ColorMe

# 用字典存储备忘录信息
'''
{
    'date':in_date,
    'thing':in_thing,
    'time':in_time
}

'''
title = ColorMe('51备忘录'.center(30,'-')).yellow()
print(title)
memo_list=[]
user =input(ColorMe('请输入用户名：').yellow())

print(f'欢迎，{user}')
choose = 'y'
all_time = 0
chos_str = ColorMe('请选择备忘录模式，1.自由模式、2.固定模式').yellow()
m = input(chos_str)

if m == '1' :
    time_dict = {
    '早上': '08点',
    '中午': '12点',
    '晚上': '20点'
    }
    excp_str = ColorMe('请用时间+事件来添加备忘录。例如：08点去上班。或中午去吃饭').yellow()
    print(excp_str)
    while choose == 'y':
        str = input(ColorMe('请输入待办事项：').yellow())
        if str.find('点') >= 0:
            in_time = str[str.find('点')-2:str.find('点')+1]
            in_thing = str[str.find('点')+1:]
        else:
            if str.find('早上') >=0:
                in_time = time_dict['早上']
                in_thing = str[str.find('上')+1:] 
            elif str.find('中午') >= 0:
                in_time = time_dict['中午']
                in_thing = str[str.find('午')+1:] 
            elif str.find('晚上') >= 0:
                in_time = time_dict['晚上']
                in_thing = str[str.find('上')+1:] 
            else:
                print('输入错误，请重新输入：')  
        
        in_dict = {}
            
        in_dict['thing'] = in_thing
        in_dict['time'] = in_time
        memo_list.append(in_dict)
        print('待办列表'.center(30,'-'))

        n = 0
        for x in memo_list:
            n += 1
            thing = x['thing']
            time = x['time']
            print(f'{n}. {time} 处理：{thing}')
        print('end'.center(30,'-'))
        print(ColorMe(f'共{n}条待办事项').yellow())
        choose = input('是否继续添加：y/n：')
    print('感谢您的使用，再见')
         
else :
    while choose == 'y':

        print('请输入备忘信息：')
        in_date = input('日期：')
        in_thing = input('事件：')
        in_time = input('用时：')
        all_time += int(in_time)

        in_dict = {}

        in_dict['date'] = in_date
        in_dict['thing'] = in_thing
        in_dict['time'] = in_time

    # one = f'{n}. {in_date},处理{in_thing},用时：{in_time}'
        memo_list.append(in_dict)
        print('待办列表'.center(30,'-'))
        n = 0
        for x in memo_list:
            n += 1
            date = x['date']
            thing = x['thing']
            time = x['time']
            print(f'{n}. {date}处理{thing},用时：{time}')
        print('end'.center(30,'-'))
        print(ColorMe(f'共{n}条待办事项，总时长：{all_time}分钟').yellow())
        choose = input('是否继续添加：y/n')
    print('感谢您的使用，再见')

