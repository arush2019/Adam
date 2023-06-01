import speech_recognition as sr
import os


def Listen():
    #"""This function listens to the user's speech and returns the recognized text."""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.... ")
        r.pause_threshold = 1 # type: ignore
        audio = r.listen(source,0,8) # type: ignore

# Recognize the speech
    try:
        print("Recognizing.... ")
        query = r.recognize_google(audio,language="hi" "en" "ban") # type: ignore

    except:
        return""
    
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    query = Listen().lower()

    if "wake up" in query:
        os.startfile(r"E:\\Adam\\Main.py")

    else:
        pass

while True:
    WakeupDetected()
