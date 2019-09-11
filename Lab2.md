# Week2 (Beginner Tasks in ns-3)

## 1. How to install specific modules in ns-3?
All information regarding installing new modules can be found in the following link
https://www.nsnam.org/docs/manual/html/new-modules.html

Step 0:

All modules are present in the ```src/``` folder.
```create-module.py``` is used to create a skeleton for a new module.
```
./create-module.py new-module-name
```
The create-module.py script will create the directories as well as initial skeleton wscript,
.h, .cc, and .rst file.


## 2. Visualize the output of ns-3 examples by using PyViz and NetAnim.
**Unable to do it**
Gives the following error after running:
```
./waf --pyrun src/flow-monitor/examples/wifi-oslr-flowmon.py --vis
```
```
Waf: Entering directory `/home/user/ns-allinone-3.30/ns-3.30/build'
Waf: Leaving directory `/home/user/ns-allinone-3.30/ns-3.30/build'
Build commands will be stored in build/compile_commands.json
'build' finished successfully (0.461s)
Traceback (most recent call last):
  File "src/flow-monitor/examples/wifi-olsr-flowmon.py", line 22, in <module>
    import ns.applications
ModuleNotFoundError: No module named 'ns'
Command ['/home/user/Abhinav-Backup/anaconda3/bin/python3', 'src/flow-monitor/examples/wifi-olsr-flowmon.py', '--SimulatorImplementationType=ns3::VisualSimulatorImpl'] exited with code 1
```
Google Code-In Task : https://codein.withgoogle.com/archive/2018/organization/5152211763986432/task/6454774882893824/

PyViz is a live simulation visulizer that uses no trace files to animate the simulation whereas NetAnim is an offline animator which animates the simulation using an XML trace file collected during simulation.

Run the first.cc example which can be found in examples/tutorial director using both PyViz and NetAnim. Provide the screenshot of output from both tools.

Reference Links:
PyViz : https://www.nsnam.org/wiki/index.php/PyViz
NetAnim : https://www.nsnam.org/wiki/index.php/NetAnim
http://code.nsnam.org/ns-3-dev/file/e6897edc9053/examples/tutorial



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
Replace the trace filename with a name of your choice.

## 7. Write your own packet sink, on-off, bulk send, UDP echo server applications. Get creative. Make sure the example highlights the type of application you’re using.
