#!/usr/bin/env/Python
# ----coding: utf-8 ------
# 51memo028.py
# test
# author: wangchen

import pickle


class Memo:
    "备忘录"
    def __init__(self, admin):
        "初始化"
        self._id = 0
        self.admin = admin
        self.name = "name"
        self.thing = "thing"
        self.date = "date"
        self.time = ""
    
    @property
    def id(self):
        "只读ID"
        return self._id
    
    
    def title(self):
        "标题"
        title = '51备忘录'.center(30, '-')
        print(title)
    
    def input_name(self):
        "输入姓名"
        self.name = input('请输入姓名：')
       
    def welcome(self):
        "欢迎词"
        print(f'欢迎：{self.name}')
    
    def judge_1(self):
        "是否是第一次使用"
        n = input('是否是第一次使用？：y/n')
        return n
    
    def menu(self):
        "菜单"
        list_dict = {
            '1': '新增',
            '2': '删除',
            '3': '修改',
            '4': '查询所有',
            '5': '退出'
}

        for k, v in list_dict.items():
            print(f'{k}:{v}', end="  ")
        
        print()
            
    def choose_menu(self):
        "选择菜单功能"
        chos = input('请输入功能编号：')       
        return chos
    
    def create_memo(self):
        "创建备忘录"
        self.title()
        self.input_name()
        self.welcome()
        if self.judge_1() == 'y':
            self.admin.save()
        else:
            self.admin.load()
                

class MemoAdmin:
    "备忘录主要方法"
    def __init__(self):
        self.memo_list = []

    def add(self):
        "增加一条备忘录"
        chos = ''
        while chos != 'y':
            print('请输入备忘信息：')
            date = input('日期：')
            thing = input('事件：')
            time = input('用时：')
            in_dict = {'date': date, 'thing': thing, 'time': time}
            self.memo_list.append(in_dict)
            chos = self.return_menu()
        self.query_all()  # 插入完后看全部数据
        self.save()  # 循环结束保存结果
        print()  # 换行，为了看起来好看
              
    def delete(self):
        "删除一条备忘录"
        chos = ""
        while chos != 'y':
            self.query_all()
            del_num = input('请输入要删除的编号：')
            self.memo_list.pop(int(del_num)-1)
            print('删除成功')
            chos = self.return_menu()
        self.query_all()
        self.save()
    
    def modify(self):
        "修改备忘录"
        chos = ""
        while chos != 'y':
            self.query_all()
            mod_num = input('请输入要修改的编号：')
            new_valu = input('请输入要修改的内容：例如：date:2.2')
            k = new_valu.split(':')
            self.memo_list[int(mod_num)-1][k[0]] = k[1]
            chos = self.return_menu()
        self.query_all()
        self.save()
    
    def query_all(self):
        "列出所有备忘录"
        print('待办列表'.center(30, '-'))
        n = 0
        for x in self.memo_list:
            n += 1
            print(f'{n}:{x}')
    
    def save(self):
        "保存"
        with open('db.pkl', 'wb') as f:
            f.write(pickle.dumps(self.memo_list))
            print("文件保存成功")
    
    def load(self):
        "读取"
        print(self.memo_list)
        with open('db.pkl', 'rb') as f:
            self.memo_list = pickle.loads(f.read())
            print("文件读取成功")

    def exit(self):
        "结束语"
        print('感谢使用，再见')
    
    def return_menu(self):
        "每个功能之后返回菜单提示"
        chos = input('是否返回菜单：y/n')
        return chos


def main():
    admin = MemoAdmin()
    memo = Memo(admin)
    memo.create_memo()
    chos = ""
    while chos != '5':
        memo.menu()
        chos = memo.choose_menu()
        if chos == '1':
            admin.add()
        elif chos == '2':
            admin.delete()
        elif chos == '3':
            admin.modify()
        elif chos == '4':
            admin.query_all()
        else: 
            admin.exit()
    
if __name__ == "__main__":
    main()