import pyttsx3
import os

# map id to get nameTh
# generate with all emotion
# filename as id_nameTH_emotionEN
# Generate for 1 Person get all emotion
def Generate_AudioFile(id: str,name_EN: str,name_TH:str):
    engine = pyttsx3.init()
    TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"

    emotion_en = ["angry" , "disgust", "fear" , "happy", "sad" , "suprise", "neutral"]
    emotion_th = ["คุณโกรธอะไรมาหรือป่าว" , "สีหน้าของคุณดูไม่ค่อยดีเลยนะ" , "คุณดูตื่นกลัวนะ" , "คุณดูมีความสุขมากนะ", "คุณเป็นอะไรหรือเปล่า ดูเศร้าๆนะ", "คุณดูตกใจนะ", "ขอให้เป็นวันที่ดีนะ"]
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.setProperty('rate', 120)  #148

    engine.setProperty('voice', TH_voice_id)
    # name = "ดร. สุวัจชัย"
    # emotion = "อารมณ์ดีนะ"
    # name_th = []
    dirname = f"./new_speech/{id}_{name_EN}"
    if os.path.exists(dirname):
        os.rmdir(dirname)
    os.mkdir(dirname)
    for i ,v in enumerate(emotion_th):
        speech = f"สวัสดี คุณ{name_TH} วันนี้ {v}"
        filepath = f"{dirname}/{emotion_en[i]}.mp3"
        engine.save_to_file(speech, filepath)
        # engine.say(speech)
        print(f"{i} || {v}")

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
        "31" : "พัททพล",
        "32" : "มิรา",
        "33" : "สุมิตรา",
        "34" : "เกื้อกูล",
        "35" : "จิระวัต",
        "36" : "ธราดล",
        "38" : "พลฉัตร",
        "40" : "พิระพัก",
        "42" : "ดร. นิกรณ์",
        "43" : "ดร. ลือพล",
        "44" : "ดร. สุวัจชัย",
        "45" : "กรพิสิท",
        "48" : "ธวัชชัย",
        "49" : "พัทรพูม",
    }
    arr_raw = os.listdir("./database")
    for v in arr_raw:
        x = v.split("_")
        id = x[0]
        name = x[1]
        if id not in name_dict:
            continue
        Generate_AudioFile(id = id,name_EN=name,name_TH=name_dict[id])