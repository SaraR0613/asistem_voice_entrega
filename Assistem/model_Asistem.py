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


engine.say("por favor ingrese un texto")
engine.runAndWait()

a = input("por favor ingrese un texto: ")

url = str("C:\Prueba")
SpeechRecognitionSystem().speak(a)
SpeechRecognitionSystem().get_datetime()
Fillemanager().open_file(url)
Fillemanager().open_notepad()
Webnavegartor().open_google_tab()


recognizer = sr.Recognizer()
mic = sr.Microphone()

engine.say("Ya puedes hablar")
engine.runAndWait()

with mic as source:

    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio, language = 'ES')
print(f'Has dicho: {text}')
