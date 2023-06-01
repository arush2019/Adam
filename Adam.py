from Brain.AiBrain import ReplyBrain
from Body.Listen import Listen
print("»Starting Teh Adam : Wait For A Seconds.... ")
from Body.Speak import Speak
from Features.Clap import Tester 
print("»Starting Teh Adam : Wait For A Seconds.... ")


def MainExecution():
    Speak("Helo Sir")
    Speak("I am Adam, I am Ready To Assist You Sir.")

    while True:
        Data = MainExecution()
        Data = str(Data)
        Reply = ReplyBrain(Data)
        Speak(Reply)


def ClapDetect():
    query = Tester()
    if "True-Mic" in query: # type: ignore
        print("")
        print("Clap Detected!! ")
        print("")
        MainExecution()

    else:
        pass

    
