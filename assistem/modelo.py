import pyttsx3
import os
import datetime

motor = pyttsx3.init()


class SpeechRecognitionSystem:

    def hablar(self, text_: str):
        motor.say(text_)
        motor.runAndWait()

    def obtener_fecha(self):
        now = datetime.datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.hablar(f"La fecha y hora actual son: {date_time_str}")

    def abrir_calendario(self):
        os.system('start outlookcal:')


class FileManager:

    def abrir_archivo(self, url_archivo: str):
        os.system(f'start {url_archivo}')

    def crear_nota(self, nombre: str, _text: str):
        with open(f'../../prueba_texto/{nombre}.txt', 'w', encoding='utf8') as note:
            note.write(_text)

    def leer_archivo(self, nombre: str):
        with open(f'../../prueba_texto/{nombre}.txt', 'r') as nota:
            leer = nota.read()
            motor.say(leer)
            motor.runAndWait()

    def abir_carpeta(self, url_carpeta: str):
        os.system(f'start {url_carpeta}')


class WebNavigator:

    def abrir_google(self):
        url = 'https://www.google.com'
        os.system(f'start {url}')
