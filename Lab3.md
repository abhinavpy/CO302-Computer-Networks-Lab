# Week 3 (Intermediate tasks in ns-3)

## 1. Use Valgrind to understand memory leaks using first.cc
https://www.nsnam.org/wiki/HOWTO_use_Valgrind_to_debug_memory_problems

Valgrind can be used to find memory leaks or errors.
```
./waf --command-template="valgrind [options] %s" --run ns-3-program-name
```
Valgrind should be used on debug, dynamically linked code (the default in ns3) and not on statically linked
or optmized code; see
https://people.gnome.org/~newren/tutorials/developing-with-gnome/html/ch03s03.html

Valgrind for ns3 is known to work on recent Linux systems that do not have gtk enabled. 

## Set breakpoints at three places in star.cc and list all of them using gdb (GNU Debugger)
## Print the data type of the variables in star.cc using gdb (GNU Debugger)
## Modify first.cc to support IPv6 addressing
## Enable support of flow monitor in tcp-bulk-send.cc
## Compare the congestion window plots for TCP Newreno and TCP Highspeed
## Install ns-3 Direct Code Execution (DCE) in advanced mode and run dce-iperf.cc example
## Add comments in at least 3 classes or examples of your choice. Get creative. Make sure somebody who is not an expert in ns-3 is able to understand the comments.