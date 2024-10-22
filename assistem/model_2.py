import pyttsx3
import os
import datetime
import pyaudio
import json
from vosk import Model, KaldiRecognizer

engine = pyttsx3.init()  # Inicialización global del motor de pyttsx3

# Cargar el modelo de Vosk (usa la ruta correcta al modelo de español)
model_path = "C:/Users/Mateo/PycharmProjects/asistem_voice/assistem/vosk-model-small-es-0.42"  # Cambia esta ruta si lo pones en otro lugar
if not os.path.exists(model_path):
    print(f"Modelo no encontrado en {model_path}")
    exit(1)

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

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

    def open_notepad(self):
        os.system('notepad')  # Abre el Bloc de notas


class WebNavigator:

    def open_google_tab(self):
        url = 'https://www.google.com'
        os.system(f'start {url}')  # Abre la URL en el navegador predeterminado


# Función para reconocer la voz usando Vosk
def recognize_speech():
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Escuchando...")
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_json = json.loads(result)
            text = result_json.get('text', '')
            if text:
                print(f"Has dicho: {text}")
                return text.lower()  # Convertir a minúsculas
        else:
            print("No se detectó una frase clara.")


# Bucle principal de comandos por voz
while True:
    engine.say("Habla")
    engine.runAndWait()

    text = recognize_speech()  # Llamamos a la función que reconoce la voz

    if text == "uno":
        engine.say("¿Qué quieres que te lea?")
        engine.runAndWait()
        a = recognize_speech()
        if a:
            SpeechRecognitionSystem().speak(a)
    elif text == "dos":
        SpeechRecognitionSystem().get_datetime()
    elif text == "tres":
        url = str("C:/Prueba")
        FileManager().open_file(url)
    elif text == "cuatro":
        FileManager().open_notepad()
    elif text == "cinco":
        WebNavigator().open_google_tab()
    elif text == "salir":
        engine.say("Hasta luego")
        engine.runAndWait()
        break
    else:
        engine.say("No se encontró opción")
        engine.runAndWait()
