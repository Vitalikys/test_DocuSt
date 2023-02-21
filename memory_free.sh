#!/bin/bash

# Version using      /proc/meminfo
#in_use_ram=`free | grep Mem | awk '{print $3/$2 * 100.0}'`
in_use_ram=`free | grep Пам | awk '{print $3/$2 * 100.0}'`
echo "memory in use: $in_use_ram %"

free_ram=`free | grep Пам | awk '{print $4/$2 * 100.0}'`
echo "free memory: $free_ram %"


if [[ $in_use_ram -gt $1 ]] # $1 is first argument
then
  curl -X POST -H "Content-Type: application/json" -d '{"value": "alarm"}' \
    http://78.27.202.55:8080/flask/memory_alarm
  echo "alarm is generated"
else
  echo "everything is OK, Ram is used under limit $1 %"
fi