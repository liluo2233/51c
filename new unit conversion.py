#!/usr/bin/env/Python
# ----coding: utf-8 ------
# new unit conversion.py
# author:wangchen


class Transfer:
    "主体程序"
    def __init__(self):
        "初始化"
        self.str = ""
    
    def welcome(self):
        "欢迎词"
        print('欢迎使用万能转换器'.center(30, '-'))
        
    def menu(self):
        "显示菜单"
        menu = {
            'T': '温度:1C或1F',
            'L': '长度:1mi或1km',
            'C': '货币1USD或1RMB'
        }
        print('本转换器支持三种形式转换：')
        n = 0
        for k, v in menu.items():
            n += 1
            print(f'{n}.{k}:{v}')
  
    def choose_menu(self):
        "输入需要转换的内容"
        self.str = input('请输入需要转换的内容：')
        return self.str
    
    def choose(self):
        "根据输入的内容选择功能"
        if self.str.endswith('C') or self.str.endswith('F'):
            temp = Temp(self.str)
            temp.judge()         
        elif self.str.endswith('mi') or self.str.endswith('km'):
            length = Length(self.str)
            length.judge()
        else:
            money = Money(self.str)
            money.judge()
   
    def exit(self):
        "控制循环，退出"
        n = input("按任意键继续，q退出")
        return n
            

class Temp:
    "温度转换"
    def __init__(self, str):
        "初始化"
        self.str = str
        
    def judge(self):
        "判断转换方式"
        if self.str.endswith('C'):
            t = float(self.str.strip('C'))
            self.c_to_f(t)
        else:
            t = float(self.str.strip('F'))
            self.f_to_c(t)
        
    def c_to_f(self, t):
        "摄氏温度转华氏温度"
        print(f'摄氏温度：{t}度 = 华氏温度： {(9/5) * t + 32}度')
        
    def f_to_c(self, t):
        "华氏温度转摄氏温度"
        print(f'华氏温度：{t}度 = 摄氏温度：{(5/9) * (t - 32)}度')
        

class Length:
    "长度转换"
    def __init__(self, str):
        "初始化"
        self.str = str
    
    def judge(self):
        "判断转换方式"
        if self.str.endswith('mi'):
            l = float(self.str.strip('mi'))
            self.mi_to_km(l)
        else:
            l = float(self.str.strip('km'))
            self.km_to_mi(l)
    
    def mi_to_km(self, l):
        "英里转千米"
        print(f'{l}mi = {l*1.61}m')
    
    def km_to_mi(self, l):
        "千米转英里"
        print(f'{l}km = {l*0.62}mi')


class Money:
    def __init__(self, str):
        "初始化"
        self.str = str
    
    def judge(self):
        if self.str.endswith('USD'):
            c = float(self.str.strip('USD'))
            self.u_to_r(c)
        else:
            c = float(self.str.strip('RMB'))
            self.r_to_u(c)
    
    def u_to_r(self, c):
        print(f'{c} USD = {c * 6.9} RMB')
    
    def r_to_u(self, c):
        print(f'{c} RMB = {c * 0.14} USD')


def main():
    trans = Transfer()
    trans.welcome()
    trans.menu()
    n = 'y'
    while n != 'q':
        trans.choose_menu()
        trans.choose()
        n = trans.exit()
    
if __name__ == "__main__":
    main()