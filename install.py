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
to_install_usr = input("\nDo you surely want to edit the .bashrc for default boot as Timez-os{this process may somehow damage your bash.bashrc file, make sure to create a backup}(Y/N): ")
main_location = os.getcwd()	
if to_install_usr == "Y" or "y":
	print("\nWARNING: Changing any file name or file location will cause errors from the bash.bashrc when loaded, do not do until needed\n")
	os.chdir(os.path.expanduser("~"))
	os.chdir("..")
	os.chdir("usr/etc")
	bash_file = open("bash.bashrc","a")
	bash_file.write("\ncd " + main_location + "\n")
	bash_file.write("\npython boot.py\n")
	bash_file.close()
	print("\nSuccessfully installed the pre-requirements for the Alpha version of Timez-os. [Optional] Re-open to refresh and load the OS.\n")
