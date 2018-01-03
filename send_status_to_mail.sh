#!/bin/bash
lines=`ps -ef  | grep httpd | wc -l `
TO_ADDRESS='PNKMR1221@gmail.com'

if [ $lines -ge 6 ]
then
   BODY="WebServer is running on `hostname`"
   echo ${BODY} | mail -s "status of webserver status"  $TO_ADDRESS
else
   BODY="WebServer is not running on `hostname`"
   echo ${BODY} | mail -s "status of webserver status"  $TO_ADDRESS
fi
