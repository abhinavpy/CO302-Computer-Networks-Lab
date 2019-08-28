Enable support of ASCII traces in first.cc and collect the statistics

Copy the following code from https://github.com/nsnam/ns-3-dev-git/blob/master/examples/tcp/tcp-bulk-send.cc

bool tracing = true;
if (tracing)
    {
      AsciiTraceHelper ascii;
      pointToPoint.EnableAsciiAll (ascii.CreateFileStream ("tcp-bulk-send.tr"));
      pointToPoint.EnablePcapAll ("tcp-bulk-send", false);
    }
    
    
 and paste it before the simulation part in first.cc
 
