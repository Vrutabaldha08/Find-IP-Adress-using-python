import socket as s

my_hostname = s.gethostname()

print('hostname is:' + my_hostname)

mt_ip = s.gethostbyname(my_hostname)

print('my_ip :' + mt_ip)