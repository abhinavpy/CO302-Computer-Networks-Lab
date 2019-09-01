# Week2 (Beginner Tasks in ns-3)

## 1. How to install specific modules in ns-3?
All information regarding installing new modules can be found in the following link
https://www.nsnam.org/docs/manual/html/new-modules.html

All modules are present in the ```src/``` folder.
```create-module.py``` is used to create a skeleton for a new module.
```
./create-module.py new-module-name
```
The create-module.py script will create the directories as well as initial skeleton wscript,
.h, .cc, and .rst file.

## 2. Visualize the output of ns-3 examples by using PyViz and NetAnim.


## 3. What are test cases and test suites in ns-3?


## 4. Ping a real host by using the emulation feature in ns-3.

## 5. Plot a Line graph for TCP congestion window (cwnd) using gnuplot.

## 6. Enable support of ASCII traces in first.cc and collect the statistics
Copy the following code from https://github.com/nsnam/ns-3-dev-git/blob/master/examples/tcp/tcp-bulk-send.cc
```
bool tracing = true;
if (tracing)
    {
      AsciiTraceHelper ascii;
      pointToPoint.EnableAsciiAll (ascii.CreateFileStream ("tcp-bulk-send.tr"));
      pointToPoint.EnablePcapAll ("tcp-bulk-send", false);
    }
``` 
    
and paste it before the simulation part in first.cc
 
## 7. Write your own packet sink, on-off, bulk send, UDP echo server applications. Get creative. Make sure the example highlights the type of application you’re using.
