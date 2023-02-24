task to check memory usage and send alarm to API is emplemented in two versions:

### Python script. memory_alarm.py
how to run: 

```shell
$ python3 memory_alarm.py --url 'http://78.27.202.55:8080/flask' --time 60 --message 'short message'
```

```shell
$ python3 memory_alarm.py --help 
```


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
takes integer argument(60) % to set limit ram usage 

depend which Linux language is installed:
* english - Mem  (from Memory)
* ukrainian - Пам (from Память)
```shell
./menory_free.sh 60
```

grep(1) — Linux manual page
https://man7.org/linux/man-pages/man1/grep.1.html