#Script to install pre requirements(proccess requires an internet connection & usually takes less than 10minutes)
import os	
try:
	os.system("apt update")
	os.system("pkg install libxml2")
	os.system("pkg install libxslt")
	os.system("pip install wheel")
	os.system("pip install mechanicalsoup")
	os.system("pip install requests")
	os.system("pip install BeautifulSoup4")
except:
	os.system("pkg install libxml2")
	os.system("pkg install libxslt")
	os.system("pip install wheel")
	os.system("pip install mechanicalsoup")
	os.system("pip install requests")