import pyttsx3
import os
import datetime


# Inicializa el motor de texto a voz
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_file(file_path):
    os.system(f'start {file_path}')

def open_google_tab():
    url = 'https://www.google.com'
    os.system(f'start {url}')

def get_datetime():
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    speak(f"La fecha y hora actual son: {date_time_str}")

def open_notepad():
    os.system('notepad')

#engine.say("por favor ingrese un texto")
#engine.runAndWait()
#a = input("por favor ingrese un texto: ")
#b = speak(a)
#c = open_file("Nuevo")
#e = open_google_tab()
#f = open_notepad()
#g = open_file("C:\Prueba")
#h = get_datetime()