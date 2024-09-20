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


