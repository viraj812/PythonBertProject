from gtts import gTTS as tts
import speech_recognition as sr
from playsound import playsound
from translation import translate_
import time
import os


def speak_(text):
    translated_text = translate_(text, "english", "hindi")
    t = tts(translated_text, lang='hi', tld='co.in', slow=True)
    t.save("./speech.mp3")
    time.sleep(1)
    path = os.path.abspath("speech.mp3")
    playsound(path)
    os.remove(path)
    time.sleep(1)


def speech_to_text_():
    result = None
    while(result==None):
        try:
            r = sr.Recognizer()
            audio_source = sr.Microphone()
            with audio_source as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening.....")
                audio = r.listen(source)
                result = r.recognize_google(audio)
                print(result)
        except Exception as e:
            print(e)
    result = translate_(result, "hindi", "english")
    return result

# speech_to_text()
# speak_("kaise hein aap")