# ！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
© Copyright 2018 The Author. All Rights Reversed.
------------------------------------------------------------
File Name: This is the Visual_system main file.
Author :
Time:2018-06-02
Description：run this file. the system will work.
------------------------------------------------------------
"""
import datetime
import time
import os, sys

sys.path.append("E:\Project\Crime prevention\OpenlawData\Visual_system\Information_Visualization")
sys.path.append("/home/OpenlawData/Visual_system")
current_path = os.getcwd()

# 方便测试使用。
if current_path == '/root':
    log = open('/home/OpenlawData/Visual_system/system log', 'a', encoding='utf8')
    path_openlaw = r'/home/OpenlawData/Visual_system/OpenLaw_cases.xlsx'
else:
    log = open('system log', 'a', encoding='utf8')
    path_openlaw = r'OpenLaw_cases.xlsx'

import MySQL

def get_date():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') ,time.time()

begin_date ,begin_time = get_date()
log.write('系统启动时间:\n'+ begin_date + "\n\n")

MySQL.write_to_MySQL(path_openlaw, log)
finish_date, finish_time = get_date()

spend_time = finish_time - begin_time
log.write('\n系统结束时间:\n'+ str(finish_date) + '\n')
log.write('\n本次运行共计花费时间:\n'+ str(spend_time)+ '秒\n')
log.write('——————————————————————————————\n')
log.close()