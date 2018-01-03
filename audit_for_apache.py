#!/bin/python
import os
import subprocess
def status_of_webserver():
    cmd = " ps -ef | grep httpd | wc -l "
    sp = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    out,err = sp.communicate()
    #print "out is: ",out, type(out)
    #print "err is: ", err
    if int(out) >= 6 :
	return "Running"
    else:
	return "Not Running"
def start_stop_web_server(cmd):
    try:
	sp = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    except Exception as e:
	print e

Apache_Home = "/usr/local/webserver"
start_stop_cmd = Apache_Home + os.sep + "bin" + os.sep + "httpd" + "  -k" 
#print "Cmd is : ", start_stop_cmd 
print"Finding the status of a Apache Web server....................."
status=status_of_webserver()
print"The webserver is {}".format(status)
if status == "Running":
    print"Do you want to stop it ? \n(enter 0 to stop)"
    request = int(raw_input())
    if request == 0:
	cmd = start_stop_cmd + " stop"
        start_stop_web_server(cmd)
   
else:
    print"Do you want to start it ? \n(enter 1 to start)"
    request = int(raw_input())
    if request == 1:
	cmd =start_stop_cmd + " start"
	start_stop_web_server(cmd)
