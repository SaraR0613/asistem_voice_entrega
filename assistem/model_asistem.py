import pyttsx3
import os
import datetime
import pyaudio
import json
from vosk import Model, KaldiRecognizer

motor = pyttsx3.init()  # Inicialización global del motor de pyttsx3


class SpeechRecognitionSystem:

    def hablar(self, text_: str):
        motor.say(text_)
        motor.runAndWait()

    def obtener_fecha(self):
        now = datetime.datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.hablar(f"La fecha y hora actual son: {date_time_str}")


class FileManager:



    def abrir_archivo(self, file_path: str):
        os.system(f'start {file_path}')  # Usa 'start' en Windows para abrir archivos

    def crear_nota(self, nombre: str, _text: str):
        with open(f'C:/Prueba/{nombre}.txt', 'w', encoding='utf8') as note:
            note.write(_text)

    def leer_archivo(self, nombre: str):
        with open(f'C:/Prueba/{nombre}.txt', 'r') as nota:
            leer = nota.read()
            motor.say(leer)
            motor.runAndWait()

    def abir_carpeta(self, url_carpeta: str):
        os.system(f'start {url_carpeta}')


class WebNavigator:

    def abrir_google(self):
        url = 'https://www.google.com'
        os.system(f'start {url}')  # Abre la URL en el navegador predeterminado
