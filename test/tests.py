import os
import pyttsx3
import pyaudio
import json
from vosk import Model, KaldiRecognizer
from assistem.model_asistem import FileManager, SpeechRecognitionSystem, WebNavigator

model_path = "C:/Users/Mateo/PycharmProjects/asistem_voice/assistem/vosk-model-small-es-0.42"
if not os.path.exists(model_path):
    print(f"Modelo no encontrado en {model_path}")
    exit(1)
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)
engine = pyttsx3.init()
p = pyaudio.PyAudio()
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

def funciones():
    engine.say("")
    engine.runAndWait()

# Bucle principal de comandos por voz
while True:
    engine.say("Habla")
    engine.runAndWait()

    text = recognize_speech()  # Llamamos a la función que reconoce la voz

    if text == "uno":
        engine.say("¿Qué quieres que te lea?")
        engine.runAndWait()
        a = recognize_speech()
        SpeechRecognitionSystem().speak(a)

    elif text == "dos":
        SpeechRecognitionSystem().get_datetime()

    elif text == "tres":
        engine.say("¿Qué nombre quieres que tenga el archivo?")
        engine.runAndWait()
        nombre = recognize_speech()

        engine.say(f"¿Qué quieres que contenga el archivo {nombre}?")
        engine.runAndWait()
        texto = recognize_speech()

        FileManager().create_note(nombre, texto)

    elif text == "cuatro":
            engine.say("¿Qué archivo quieres abrir")
            engine.runAndWait()
            nombre = recognize_speech()

            url = f"C:/Users/Mateo/PycharmProjects/asistem_voice/Archivos/{nombre}.txt"
            FileManager().open_file(url)

    elif text == "cinco":
        WebNavigator().open_google_tab()

    elif text == "salir":
        engine.say("Hasta luego")
        engine.runAndWait()
        break
    else:
        engine.say("No se encontró opción")
        engine.runAndWait()