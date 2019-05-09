#!/bin/sh
count=0
echo "Waiting for server to start..."
while true
do
  if [ $count -le 50 ]; then
    wget --spider -q http://xlr:5516 
    if [ $? -ne 0 ] ;then 
      echo "waiting $count"
      sleep 5
      count=$(( count+1 ))
    else 
      echo "Website is up"
      python credentials_updater.py "/keys/petportal-credentials.conf"
      exit $?
    fi
  else
    echo "Timeout exceeded...giving up waiting for website"
    exit 1
  fi
done
