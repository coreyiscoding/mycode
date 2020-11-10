#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#possible solution without calling the data 
#print("The IP addresses are 10.0.0.1 and 10.20.30.1" )

##need to figure out how to get from positions 3 and 4
#print("The IP adresses are (IP's): " + new_list[3:4] )

print("The Ip addresses are: " + new_list[4] )
