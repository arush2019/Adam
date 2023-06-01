"""This module contains code to listen to speech and translate it into another language."""

import speech_recognition as sr
from googletrans import Translator



def Listen():
    """This function listens to the user's speech and returns the recognized text."""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.... ")
        r.pause_threshold = 1 # type: ignore
        audio = r.listen(source,0,8) # type: ignore

# Recognize the speech
    try:
        print("Recognizing.... ")
        query = r.recognize_google(audio,language="hi") # type: ignore

    except:
        return""
    
    query = str(query).lower()
    return query



 
# Translate the hide to english

def Translet_hinde_to_english(Text):
    line = (str(Text))
    translator = Translator( )
    result = translator.translate(line, src="hi", dest="en")
    data = result.text 
    print(f"you : {data}.")
    return data

#  connect

def Execution():
    query = Listen()
    Line = len(query)

    if (Line>1):

        data = Translet_hinde_to_english(query)
        return data
    
    else:
        pass


while True:
    Execution()


