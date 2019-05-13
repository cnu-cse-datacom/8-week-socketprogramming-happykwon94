from socket import *
import sys
import os

s = socket(AF_INET, SOCK_DGRAM)
file_name = input("Input your file name : ")
host = "192.168.0.170" #host address or From address
port = 9999 #port number
buf = 1024
addr = (host, port)

f = open(file_name,"rb") # file open

data = f.read(buf) # data = Read 1024 from the file

fileSize = os.path.getsize(file_name)

s.sendto(file_name.encode(), addr)
s.sendto(str(fileSize).encode(), addr)

total = 0

if(data):
    print ("File Transmit Start...");
    while (data):
        total += s.sendto(data,addr)
        print("current_size / total_size =" , total,'/',fileSize, ',', float(total/fileSize)*100, '%');
        data = f.read(buf) # data = Read 1024 from the file
    print("OK")
    print("File_Send_End")
s.close()
f.close()
