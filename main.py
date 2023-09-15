import pyttsx3
import os
engine = pyttsx3.init()

TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"

engine.setProperty('volume', 0.9)  # Volume 0-1
engine.setProperty('rate', 130)  #148

engine.setProperty('voice', TH_voice_id)
# name = "ดร. สุวัจชัย"
# emotion = "อารมณ์ดีนะ"
# speech = f"สวัสดี คุณ {name} วันนี้ คุณดู{emotion}"
speech = "ไอเก่ง เขาไม่รักมึงหรอก ไอโง่"
engine.say(speech)
# engine.save_to_file(speech, './new_speech/speech.mp3')

engine.runAndWait()


# map id to get nameTh
# generate with all emotion
# filename as id_nameTH_emotionEN


arr_raw = os.listdir("./database")
for v in arr_raw:
    print(v)
    x = v.split("_")
    print(x)
def Generate_AudioFile(name: str , emotion : str) -> str:
    filepath = ""
    return filepath