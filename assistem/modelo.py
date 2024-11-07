import json
from importlib.resources import files

import pyaudio
import pyttsx3
import os
import datetime
import pywhatkit
from vosk import Model, KaldiRecognizer

motor = pyttsx3.init()


class SpeechRecognitionSystem:

    def reconocer_voz(self):

        parche_vosk = str(files("dependencia_vosk").joinpath("vosk-model-es"))
        if not os.path.exists(parche_vosk):
            print(f"Modelo no encontrado en {parche_vosk}")
            exit(1)

        modelo = Model(parche_vosk)
        reconocedor = KaldiRecognizer(modelo, 16000)

        mic = pyaudio.PyAudio()
        reproducir = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        reproducir.start_stream()
        print("Escuchando...")
        while True:
            data = reproducir.read(4096, exception_on_overflow=False)
            if reconocedor.AcceptWaveform(data):
                resultado = reconocedor.Result()
                resultado_json = json.loads(resultado)
                texto = resultado_json.get('text', '')
                if texto:
                    print(f"Has dicho: {texto}")
                    return texto.lower()  # Convertir a minúsculas

    def funciones(self):
        motor.say("si quieres que te lea algo di uno\n"
                  "si quieres que te diga la hora y el dia di dos\n"
                  "si quieres crear un archivo de texto con algo di tres\n"
                  "si quieres abrir un archivo de texto di cuatro\n"
                  "si quieres que te lea un archivo de los ya existentes di cinco"
                  "si quieres abrir google di seis\n"
                  "si quieres abrir la carpeta donde se encuentran tus archivos di siete\n"
                  "si quieres abrir el calendario di ocho\n"
                  "si quieres enviar un mensaje di nueve\n"
                  "si quieres dejar de usar di salir\n"
                  "si quieres que repita todo de nuevo di repite")
        motor.runAndWait()

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

    def crear_nota(self, nombre_archivo: str, _text: str):
        ubicacion_carpeta = str(files("prueba_texto").joinpath(f"{nombre_archivo}.txt"))
        with open(ubicacion_carpeta, 'w', encoding='utf8') as note:
            note.write(_text)

    def leer_archivo(self, nombre_archivo: str):
        ubicacion_carpeta = str(files("prueba_texto").joinpath(f"{nombre_archivo}.txt"))
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
                                            "luján": "+573212443269"}

        hora: int = datetime.datetime.now().hour
        minutos: int = datetime.datetime.now().minute

        numero_elegido: str = numeros_telefono[nombre]
        pywhatkit.sendwhatmsg(numero_elegido, mensaje, hora, minutos)
