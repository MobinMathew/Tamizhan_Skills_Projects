# Project 4:
# Port Scanner

# DISCLAIMER:
This tool is created fo educational purposes only.
Do not use it on any system o network without explicit permission.
Unauthorized scanning is illegal and unethical.

# Descripion:
This project is a `Port Scanner` built with Python. It scans a given IP address or domain name for open TCP ports within a user-specified range. It uses `multithreading` to speed up the scanning process significantly.

# Features:
-> Scans arange of ports on a target IP or domain
-> Uses threading to scan muliple ports in parallel
-> Identifies and  prints open ports
Lightweight and fast

# Code Explanation:

  import socket
  import threading

-> socket : This is used to create network connections specifically to check whether a port is open or closed.
-> threading : This module allows the scanner to run multiple port scan in parallel, speeding up the entire process.

  target = input("Enter the IP address or domain to scan:")

-> The target IP or domain name.

  start_port = int(input("Enter the starting port number:"))

-> The starting port number : the first port to being scanning.

  ending_port = int(input("Enter the ending port number:"))

-> These inputs let the user contol the scan range based on what they want to investigate.

  def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)# set 1 second timout
        result = sock.connect_ex((ip, port)) # try to connecting to the port 
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()
    except:
        pass

-> This is the main function that will scan a single port on the given Ip address.
-> Inside the function, I first create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
-> This socket is used to attempt a connection to the target port.
-> Set a timeout of 1 second so that the program doesn't reply within 1 secpnd its considered closed or filtered.
-> Then it tries o connect to the given IP and Port.
-> If the result is 0, it means the port is open and it print that information to the terminal.
-> Whether th port is open or not, we close the socket to freeup system resources.
-> If any error occurs like a bad address or a connection issue we silently ignore it using except : pass
-> This keeps the program running smoothly without crashing 

  threads = []

-> Then I created an empty list called threads to keep track of all the threads I'll belaunching for port scanning.

  for port in range(start_port, ending_port +1):
    t = threading.Thread(target=scan_port, args=(target, port))
    threads.append(t)
    t.start()

-> This for loop goes through every port number in the user-specified range from the starting to the ending port.
-> For each port, I create a new thread.
-> The taget is the scan_port fucntion and the argument are the `IP (target)` and `port`.
-> This means each thread will scan one specific port independently.
-> I add the thread to the thread list then immediately start it using `.start()` 
-> This allows all port scans to happen in parallel, which is much faster than scanning one port at a time.

  for t in threads:
    t.join()

 -> After the staring all the threads, I use `.join()` to wait for each one to finsih.
 -> This ensure the program doesn't exit before all port scans are complete. 

 # What I learned:

 -> How TCP connections work at the port level.
 -> How to use Python's `socket` and `threading` modules.
 -> The importance of ethical practices in cybersecurity.

# Author:
 Mobin Mathew
 Tamizhan Skills RISE Cybersecurity & Ethical Hacking Intern