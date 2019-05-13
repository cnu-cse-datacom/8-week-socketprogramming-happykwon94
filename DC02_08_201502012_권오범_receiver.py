from socket import *
import select

host = "192.168.0.170" # where to get it name = "cse-411"
port = 9999

s = socket(AF_INET, SOCK_DGRAM) # make socket
s.bind((host, port)) #ip address, port number assignment

addr = (host, port) # For ease of use
buf = 1024 # byte unit
print("file recv start from ", host)

data, addr = s.recvfrom(buf) # Received as much as 1024
print(data)
file_name = data.decode()
print("File Name : ", file_name)
f = open(data.strip(), 'wb')

data, addr = s.recvfrom(buf)
file_size = data.decode()
print("File Size : ", file_size)

data, addr = s.recvfrom(buf) # Received as much as 1024
total = 0

try:
    while(data): # success
        total += len(data.decode()) # length
        print("current_size / total_size =" , total,'/',file_size, ',', float(total/int(file_size))*100, '%');
        f.write(data) # write
        s.settimeout(2)
        data, addr = s.recvfrom(buf)
except timeout: # exception handling
        f.close()
        s.close()
        print ("File Download Finish")
