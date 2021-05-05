#Timez'os alpha version
#Startup/Boot file
import os
#Main run looper
x = 1
#Required->linecache, time, os<-
main_location = os.getcwd()
print("\033[1;37;46mWelcome, user.")
try:
	os.system("python timez-os.sourcecode")
except:
	x = 0	