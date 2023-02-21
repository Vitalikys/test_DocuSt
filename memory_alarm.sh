#!/bin/bash
# Version using      /proc/meminfo
# select 2nd column  = 16281488
# awk вибираємо колонку значення за номером( майже як csv)
total_ram=`grep MemTotal /proc/meminfo | awk '{print $2}'`
free_ram=`grep MemAvailable /proc/meminfo | awk '{print $2}'`
used_ram=$(expr $total_ram - $free_ram)

#echo "total mem = $total_ram"
#echo "free mem = $free_ram"
#echo "used mem = $used_ram"


in_use_percent_ram=$(( $used_ram / $total_ram ))
let "in_use_percent_ram = $(( used_ram * 100 / total_ram ))"

echo "current RAM - in use percent $in_use_percent_ram"

#if [[ $in_use_percent_ram -gt 70 ]]
if [[ $in_use_percent_ram -gt $1 ]] # $1 is first argument
then
  curl -X POST -H "Content-Type: application/json" -d '{"value": "alarm"}' \
    http://78.27.202.55:8080/flask/memory_alarm
  echo "alarm is generated"
else
  echo "everything is OK, Ram is used under limit $1 %"
fi