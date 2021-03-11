import pyttsx3
#import subprocess

engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')

def text_to_speech(text):
    fn = "data/voice.mp3"
    fout = "data/voice.ogg"
    engine.save_to_file(text, fn)
    engine.runAndWait()
#    subprocess.run(["ffmpeg", "-i", fn, "-c:a", "libopus", "-b:a", "bitrate", fout])
    return fn
