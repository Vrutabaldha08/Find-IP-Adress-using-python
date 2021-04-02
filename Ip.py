#Find IP Adress using python


#Import the necessary packages 
import socket as s

#get my hostname
my_hostname = s.gethostname()

#display my hostname
print('hostname is:' + my_hostname)


#get my IP
my_ip = s.gethostbyname(my_hostname)

#display my IP
print('my_ip :' + my_ip)


#set the hostname
host = 'paruluniversity.com'

#fetch IP Adress
ip = s.gethostbyname(host)

#display the IP Adress
print('The IP Adress of ' +host+ ' is : ' + ip)