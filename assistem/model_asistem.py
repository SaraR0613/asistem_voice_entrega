import pyttsx3
import os
import datetime
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init()
p = pyaudio.PyAudio()

class SpeechRecognitionSystem:

    def speak(self, text_: str):
        pyttsx3.init().say(text_)
        pyttsx3.init().runAndWait()

    def get_datetime(self):
        now = datetime.datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        pyttsx3.speak(f"La fecha y hora actual son: {date_time_str}")


class Fillemanager:

    def open_file(self, file_path: str):
        os.system(f'start {file_path}')

    def open_notepad(self):
        os.system('notepad')


class Webnavegartor:

    def open_google_tab(self):
        url = 'https://www.google.com'
        os.system(f'start {url}')


#engine.say("por favor ingrese un texto")
#engine.runAndWait()

while True:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    """engine.say("si quieres que te lea algo di uno\n"
               "si quieres que te diga la hora y el dia di dos\n"
               "si quieres abrir una carpeta di tres\n"
               "si quieres abrir un nuevo blog de notas di cuatro\n"
               "si quieres abrir google di cinco")
    engine.runAndWait()"""
    engine.say("habla")
    engine.runAndWait()
    with mic as source:
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language = 'ES')

    if text == "uno":
        engine.say("que quieres que te lea")
        engine.runAndWait()
        with mic as source:
            audio = recognizer.listen(source)
        a = recognizer.recognize_google(audio, language='ES')
        SpeechRecognitionSystem().speak(a)
    elif text == "dos":
        SpeechRecognitionSystem().get_datetime()
    elif text == "tres":
        url = str("C:\Prueba")
        Fillemanager().open_file(url)
    elif text == "cuatro":
        Fillemanager().open_notepad()
    elif text == "cinco":
        Webnavegartor().open_google_tab()
    elif text == "salir":
        engine.say("Hasta luego")
        engine.runAndWait()
        break
    else:
        engine.say("No se encontro opcion")
        engine.runAndWait()
print(text)