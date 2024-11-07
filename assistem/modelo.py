from importlib.resources import files
import pyttsx3
import os
import datetime
import pywhatkit

motor = pyttsx3.init()


class SpeechRecognitionSystem:

    def dictado(self, text_: str):
        motor.say(text_)
        motor.runAndWait()

    def obtener_fecha(self):
        now = datetime.datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.dictado(f"La fecha y hora actual son: {date_time_str}")

    def abrir_calendario(self):
        os.system('start outlookcal:')


class FileManager:

    def abrir_archivo(self, url_archivo: str):
        os.system(f'start {url_archivo}')

    def crear_nota(self, nombre: str, _text: str):
        ubicacion_carpeta = str(files("prueba_texto").joinpath(f"{nombre}.txt"))
        with open(ubicacion_carpeta, 'w', encoding='utf8') as note:
            note.write(_text)

    def leer_archivo(self, nombre: str):
        ubicacion_carpeta = str(files("prueba_texto").joinpath(f"{nombre}.txt"))
        with open(ubicacion_carpeta, 'r') as nota:
            leer = nota.read()
            motor.say(leer)
            motor.runAndWait()

    def abir_carpeta(self, url_carpeta: str):
        os.system(f'start {url_carpeta}')


class WebNavigator:

    def abrir_google(self):
        url = 'https://www.google.com'
        os.system(f'start {url}')

    def enviar_mensaje(self, nombre: str, mensaje: str):
        numeros_telefono: dict[str, str] = {"kevin": "+573054449333",
                                            "sara": "+573027334821",
                                            "lujan": "+573212443269"}

        hora: int = datetime.datetime.now().hour
        minutos: int = datetime.datetime.now().minute

        numero_elegido: str = numeros_telefono[nombre]
        pywhatkit.sendwhatmsg(numero_elegido, mensaje, hora, minutos)
