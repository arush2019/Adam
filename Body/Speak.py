#from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#from time import sleep
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By

import pyttsx3


def Speak(Text):
    engin = pyttsx3.init("sapi5")
    voices = engin.getProperty('voices')
    engin.setProperty('voices', voices[1].id)
    engin.setProperty('rate',170)
    engin.say(Text)
    engin.runAndWait()
   

Speak("hello")


#chrome_options = Options()
#chrome_options.add_argument('--log-level=3')
#chrome_options.headless = True
#PathofDriver = "Driver\\chromedriver.exe"
#driver = webdriver.Chrome(PathofDriver,options=chrome_options)
#driver.maximize_window()

#Website = f'https://ttsmp3.com/text-to-speech/British%20English/'

#driver.get(Website)
#ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
#ButtonSelection.select_by_visible_text('British English / Brian')

#def Speak(Text):
    #print("")
    #print(f" AI : {Text}.")
    #print("")
    #Data = str(Text)
    #xpathtec = '/html/body/div[4]/div[2]/form/textarea'
    #driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
    #driver.find_element(by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
    #driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
    #sleep(2)

# Pyttsx3 - Module
# Os Based Framework


