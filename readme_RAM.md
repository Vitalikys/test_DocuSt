grep(1) — Linux manual page
https://man7.org/linux/man-pages/man1/grep.1.html

### Bash Script. Version using   /proc/meminfo
save all data about RAM to file
```shell
cat /proc/meminfo > memory_all.txt
```

```shell
chmod +x memory_alarm.sh
```

#### How run script. 
70 - is percent argument to set limit 
```shell
./memory_alarm.sh 70
```

#### Description to arguments 
* MemFree: free RAM, the memory which is not used for anything at all. 
* MemAvailable: available RAM, the amount of memory available for allocation to any process.


### Bash Script. Version using   $ Free

