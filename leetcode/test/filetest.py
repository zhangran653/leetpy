# -*- coding : utf-8 -*-
import time

import pandas as pd

print(111)

chat = pd.read_csv('/Users/zhangran/Desktop/message.csv', encoding='gb18030', sep=',', usecols=[6, 7, 8])

myGirl = ''
chat_time = []
chat_content = []
for i in range(len(chat) - 1):
    content = chat[i:i + 1]
    if content['talker'].values[0] == myGirl:
        t = content['createTime'].values[0] // 1000  # 除以1000用以剔除后三位0
        c = content['content'].values[0]
        chat_time.append(t)
        chat_content.append(c)


def to_hour(t):
    struct_time = time.localtime(t)  # 将时间戳转换为struct_time元组
    hour = round((struct_time[3] + struct_time[4] / 60), 2)
    return hour


hour_set = [to_hour(i) for i in chat_time]
