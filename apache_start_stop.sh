#!/bin/bash
#echo "Enter your apache Home"
#read -p "Enter you Apache Home: " Apache_Home
Apache_Home=/usr/local/webserver
echo "The Apache_Home is: $Apache_Home"
lines=`ps -ef | grep httpd | wc -l`
#echo "The no of lines are: $lines"

if [ $lines -ge 6 ]
then
    echo "The apache up and running"
    echo "If you want to stop enter: stop"
    read request
    if [ $request == "stop" ]
    then
	${Apache_Home}/bin/httpd -k stop
    fi
else
    echo "The apache is not ruuning"
    echo "If you want to start enter: start"
    read request
    if [ $request == "start" ]
    then
	${Apache_Home}/bin/httpd -k start
    fi

fi


