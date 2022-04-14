from vars import *
from PIL import ImageGrab
def screenshot():
    im =ImageGrab.grab()
    im.save(f'{ss_path}\\{screenshot_information}')
