#!/usr/bin/python3
# Mark Nesbitt
# 20170825

import threading
import socket
import re
import sys
import time

def porthit(host, port):
    try:#this try-except block didn't actually solve the problem.  Why not? Error: libgcc_s.so.1 must be installed for pthread_cancel to work   Aborted (core dumped)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        time.sleep(3)
        print("sleeping 3")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((host, port))
        print("SERVICE:"+str(port))
        s.shutdown()
    except:
        print("NOSERVICE:"+str(port))

def main():
    args = sys.argv[1:]
    if not len(args) == 3:
        print("Usage: ",sys.argv[0],"host","startport","endport")
        sys.exit(1)
    print(args[0])
    try:
        startport = int(args[1])
        endport = int(args[2])
    except ValueError:
        print("ports must be defined as integers")
        sys.exit(1)

    for i in range(startport, endport+1):
        if i % 100 == 0: #this if statement is what it took to stop the errors.  What's the deal?
            time.sleep(2)
            print("Sleeping 2")
        try:#This try-except block didn't actually stop the problem.  Why? 
            T = threading.Thread(target=porthit, args=(args[0],i)) 
            T.start()
        except OSError:
            time.sleep(5)
            print("Sleeping 5")
            T = threading.Thread(target=porthit, args=(args[0],i))
            T.start()

if __name__ == '__main__':
    main()
