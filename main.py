import pyttsx3
import os
import shutil
import random

# map id to get nameTh
# generate with all emotion
# filename as id_nameTH_emotionEN
# Generate for 1 Person get all emotion
def Generate_AudioFile(dirname: str,name_TH:str, emotionList_en:[str] , emotionList_th):
    engine = pyttsx3.init()
    TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.setProperty('rate', 130)  #148
    engine.setProperty('voice', TH_voice_id)
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)
    for i ,val in enumerate(emotionList_th):
        rand = random.randint(0,2)
        speech = f"สวัสดี {name_TH} วันนี้ {val[rand]}"
        filepath = f"{dirname}/{emotionList_en[i]}.mp3"
        print( i , " || ", speech)
        engine.save_to_file(speech, filepath)
    engine.runAndWait()
    return

def GenerateDefaultAudio():
    engine = pyttsx3.init()
    TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.setProperty('rate', 130)  #148
    engine.setProperty('voice', TH_voice_id)
    dirname = f"./new_speech/default"
    if os.path.exists(dirname):
         shutil.rmtree(dirname)
    os.mkdir(dirname)
    default_audio = ["คุณอุณหภูมิสูงกว่าปกติ" , "คุณอุณหภูมิปกติ", "ไม่สามารถประมวลผลได้"]
    default_name = ["mask_high", "normal_mask", "notprocess"]
    for i , speech in enumerate(default_audio):
        filepath = f"{dirname}/{default_name[i]}.mp3"
        engine.save_to_file(speech, filepath)
    engine.runAndWait()
    return

if __name__ == "__main__":
    name_dict = {
        "25" : "เสาวนี",
        "26" : "กมลรัตน์",
        "27" : "กาญศายา",
        "28" : "ณิชาภา",
        "29" : "ทักศินา",
        "30" : "ธนภร",
        "31" : "พัททะพล",
        "32" : "มิรา",
        "33" : "สุมิตรา",
        "34" : "เกื้อกูล",
        "35" : "จิระวัต",
        "36" : "ธราดล",
        "38" : "พลฉัตร",
        "40" : "พิระพัก",
        "42" : "ดร. นิกร",
        "43" : "ดร. ลือพล",
        "44" : "ดร. สุวัจชัย",
        "45" : "กรพิสิท",
        "48" : "ธวัชชัย",
        "49" : "พัทระพูม",
    }
    emotion_en = ["Happy" , "Sad", "Surprise" , "Neutral", "Angry" , "Fear"]
    emotion_th = ["คุณโกรธอะไรมาหรือป่าว", "คุณดูตื่นกลัวนะ" , "คุณดูมีความสุขมากนะ", "คุณเป็นอะไรหรือเปล่า ดูเศร้าๆนะ", "คุณดูตกใจนะ", "ขอให้เป็นวันที่ดีนะ"]
    emotionTH = [ 
        ["อารมณ์ดีนะครับ"	,"ดูแจ่มใสนะครับ"	,"ดูสดชื่นดีจังครับ"],
        ["ดูแลสุขภาพด้วยนะครับ",	"อย่าลืมทานข้าวให้ตรงเวลานะครับ",	"ดูแลจิตใจตัวเองด้วยนะครับ"],
        ["มีเรื่องให้ตื่นเต้นหรอครับ",	"กำลังลุ้นอะไรอยู่หรอครับ",	"ดูมีชีวิตชีวานะครับ"],
        ["ขอให้เป็นวันที่ดีนะครับ","อย่าลืมออกกำลังกายบ้างนะครับ","ดูสบายๆนะครับ"],
        ["ทานน้ำเยอะๆช่วยลดอุณหภูมิในร่างกายนะครับ","ถ้าหงุดหงิดบ่อยๆแก่ก่อนวัยนะครับ","โกรธอะไรอยู่หรือเปล่า ใจเย็นๆนะครับ"],
        ["มีอะไรกังวลอยู่ไหมครับ","ถ้ามีอะไรไม่สบายใจอย่าเก็บไว้คนเดียวนะครับ","หาเวลาไปพักผ่อนบ้างนะครับ"],
        ]
    arr_raw = os.listdir("./database")
    for v in arr_raw:
        x = v.split("_")
        id = x[0]
        name = x[1]
        if id not in name_dict:
            continue
        dirname = f"./new_speech/{id}_{name}"
        Generate_AudioFile(dirname=dirname,name_TH="คุณ"+name_dict[id],emotionList_en=emotion_en, emotionList_th=emotionTH)
    Generate_AudioFile(dirname=f"./new_speech/stranger", name_TH="",emotionList_en=emotion_en,emotionList_th=emotionTH)
    GenerateDefaultAudio()
    
