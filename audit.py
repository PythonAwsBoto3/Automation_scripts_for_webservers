#!/bin/python
import os
import platform
def find_path(bin_file,path):
   for root,dirs,files in os.walk(path):
       for each in files:
	   if each == bin_file:
		path_is=os.path.join(root,each)
		print"The {}  file location is: {}".format(bin_file,path_is)   
		print"The configuration file location is: ", os.path.join(os.path.dirname(path_is),"conf","httpd.conf")
print"This will find the path of the httpd/httpd.exe file location"
print"Finding the type of the system......"
print"The Opertaing system is identified as: ", platform.system()
if platform.system() == "Linux":
   print"Finding the path of the httpd location"
   find_path("httpd","/")
else:
   print"Finding the path of the httpd.exe location"
   find_path("httpd.exe","c:/")



