# -*- coding: utf-8 -*-
# @Time : 2020/9/2
# @Author : 三号菜鸟
# @File : main.py
import os

print("木总是我儿子")
temp = input("木总是我儿子吗：")
if temp == "是的":
    print("木总是我的儿子")
else:
    print("木总是大家的儿子")
backinfo = os.system('ping -t -w 1 127.0.0.1')
print(backinfo)

if __name__ == '__main__':
    main()