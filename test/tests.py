import os
import pyttsx3
import pyaudio
import json
from vosk import Model, KaldiRecognizer
from assistem.model_asistem import FileManager, SpeechRecognitionSystem, WebNavigator

parche_vosk = "C:/Users/Mateo/PycharmProjects/asistem_voice/assistem/vosk-model-small-es-0.42"
if not os.path.exists(parche_vosk):
    print(f"Modelo no encontrado en {parche_vosk}")
    exit(1)

modelo = Model(parche_vosk)
reconocedor = KaldiRecognizer(modelo, 16000)

motor = pyttsx3.init()
motor.setProperty("rate", 160)
p = pyaudio.PyAudio()


# Función para reconocer la voz usando Vosk
def reconocer_voz():
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


def funciones():
    motor.say("si quieres que te lea algo di uno\n"
              "si quieres que te diga la hora y el dia di dos\n"
              "si quieres crear un archivo de texto con algo di tres\n"
              "si quieres abrir un archivo de texto di cuatro\n"
              "si quieres abrir google di cinco\n"
              "si quieres abrir la carpeta donde se encuentran tus archivos de seis\n"
              "si quieres dejar de usar di salir\n"
              "si quieres que repita todo de nuevo di repite")
    motor.runAndWait()


funciones()

# Bucle principal de comandos por voz
while True:
    motor.say("te escucho")
    motor.runAndWait()

    text = reconocer_voz()

    if text == "uno":
        motor.say("¿Qué quieres que te lea?")
        motor.runAndWait()
        a = reconocer_voz()
        SpeechRecognitionSystem().hablar(a)

    elif text == "dos":
        SpeechRecognitionSystem().obtener_fecha()

    elif text == "tres":
        motor.say("¿Qué nombre quieres que tenga el archivo?")
        motor.runAndWait()
        nombre = reconocer_voz()

        motor.say(f"¿Qué quieres que contenga el archivo {nombre}?")
        motor.runAndWait()
        texto = reconocer_voz()

        FileManager().crear_nota(nombre, texto)

    elif text == "cuatro":
        motor.say("¿Qué archivo quieres abrir")
        motor.runAndWait()
        nombre = reconocer_voz()

        url = f"C:/Prueba/{nombre}.txt"
        FileManager().abrir_archivo(url)

    elif text == "cinco":
        motor.say("¿que archivo quieres que lea")
        motor.runAndWait()

        nombre = reconocer_voz()
        FileManager().leer_archivo(nombre)

    elif text == "seis":
        WebNavigator().abrir_google()

    elif text == "siete":
        url = str("C:\Prueba")
        FileManager().abir_carpeta(url)

    elif text == "salir":
        motor.say("Hasta luego")
        motor.runAndWait()
        break

    elif text == "repite":
        funciones()

    else:
        motor.say("No se encontró opción")
        motor.runAndWait()
