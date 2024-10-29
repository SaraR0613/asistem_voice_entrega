import pyttsx3
import os
import datetime
import pyaudio
import json
from vosk import Model, KaldiRecognizer

engine = pyttsx3.init()  # Inicialización global del motor de pyttsx3
class SpeechRecognitionSystem:

    def speak(self, text_: str):
        engine.say(text_)  # Reutiliza el motor inicializado
        engine.runAndWait()

    def get_datetime(self):
        now = datetime.datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.speak(f"La fecha y hora actual son: {date_time_str}")  # Usa el método speak


class FileManager:

    def open_file(self, file_path: str):
        os.system(f'start {file_path}')  # Usa 'start' en Windows para abrir archivos

    def create_note(self, nombre: str, _text: str):
        with open(f'C:/Prueba/{nombre}.txt', 'w', encoding='utf8') as note:
            note.write(_text)

    def open_folder(self, file):
        os.system(f'start {file}')

class WebNavigator:

    def open_google_tab(self):
        url = 'https://www.google.com'
        os.system(f'start {url}')  # Abre la URL en el navegador predeterminado
