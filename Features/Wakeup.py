import speech_recognition as sr
import os

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio =r.listen(source,0,8)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="hi")

    except:
        return""
    
    query=str(query).lower()
    return query

def WakeupDetected():
    queery= Listen().lower()

    if "wake up" in queery:
        os.startfile(r"D:\Jarvis Ai\Main.py")

    else:
        pass


while True:
    WakeupDetected()
