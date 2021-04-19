from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import speech_recognition as sr
from bs4 import BeautifulSoup
import pyttsx3
import logging


def DMStartVoice(DT,DM_title):
    DT.NavigateDM(DM_title)
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic , duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                if(text == "exit"):
                    break
                elif(text.startswith("chat ")):
                    DT.Chat(text[5:])	
                    logging.info(f"Chatted : {text[5:]}")
                logging.info(f"Recognised : {text}")
        except:
            logging.error("Excepted : Voice Recognition API Failed.")
            recognizer = sr.Recognizer()
            continue


def GuildStartVoice(DT,guild ,indx):
    DT.NavigateChannelByIndex(guild , indx)
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic , duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                if(text == "exit"):
                    break
                elif(text.startswith("chat ")):
                    DT.Chat(text[5:])	
                    logging.info(f"Chatted : {text[5:]}")
                logging.info(f"Recognised : {text}")
        except:
            logging.error(f"Excepted : Voice Recognition API Failed.")
            recognizer = sr.Recognizer()
            continue


