import speech_recognition as sr
import os
from Adam import MainExecution

def Listen():
    #"""This function listens to the user's speech and returns the recognized text."""
    r = sr.Recognizer()

    with sr.Microphone() as source:
         print("Listening.... ")
         r.pause_threshold = 1 
         audio = r.listen(source,0,8) 

# Recognize the speech
    try:
        print("Recognizing.... ")
        query = r.recognize_google(audio,language= "en") 

    except:
        return""
    
    query = str(query).lower()
    print(query)
    return query


def Wakeup_Detected():
    query = Listen().lower()

    if "Wake up" in query:
        print("wake up Datected. ")
        MainExecution()

    else:
        pass

Wakeup_Detected()
