from scipy.io.wavfile import write
import sounddevice as sd
from vars import *
#from threading import Thread
def record():
    fs = audio_sample_freq
    seconds = audio_time

    myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels=2)
    sd.wait()

    write(f'{audio_path}\\{audio_information}',fs,myrecording)

