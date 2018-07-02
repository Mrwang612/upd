#!/user/bin/Python3
# -*- coding:utf-8 -*-
# Author:Gangnam
# Time:2018.6.30
str1 = "sadaswqsavvcxsdwcvxvcds"
str2 = ""
for i in str1:
    if not i in str2:
        str2 += i
print(str2)
list1 =list(set(str1))
list1.sort()
for i in list1:
    str2 += i
print(str2)
list1 = [1,2,3,4] # 列表转化字符串
str1 = str(list1)
print(str1)
print(type(str1))

from socket import *
while True:
    udp_socket =socket(AF_INET,SOCK_DGRAM)
    dest_addr =('192.168.21.104', 8080)
    send_data = input("请输入要发送的数据：")
    udp_socket.sendto(send_data.encode("utf - 8"),dest_addr)
    udp_socket.close()

创建upd套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)
# 准备接收方的地址
dest_addr = ("192.168.21.104",8080)
send_data = input("请输入要发送的数据：")
udp_socket.sendto(send_data.encode("utf - 8"),dest_addr)
recv_data = udp_socket.recvfrom(1024)
print(recv_data[0].decode("gbk"))
print(recv_data[1])
udp_socket.close()
