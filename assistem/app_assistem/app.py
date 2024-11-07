import os
from importlib.resources import files
import pyttsx3
import pyaudio
import json
from vosk import Model, KaldiRecognizer
from assistem.modelo import FileManager, SpeechRecognitionSystem, WebNavigator

parche_vosk = str(files("dependencia_vosk").joinpath("vosk-model-es"))
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
              "si quieres que te lea un archivo de los ya existentes di cinco"
              "si quieres abrir google di seis\n"
              "si quieres abrir la carpeta donde se encuentran tus archivos di siete\n"
              "si queires abrir el calendario di ocho\n"
              "si quieres dejar de usar di salir\n"
              "si quieres que repita todo de nuevo di repite")
    motor.runAndWait()


if __name__ == "__main__":
    funciones()
    while True:
        motor.say("te escucho")
        motor.runAndWait()

        text = reconocer_voz()

        if text == "uno":
            motor.say("¿Qué quieres que te lea?")
            motor.runAndWait()
            a = reconocer_voz()
            SpeechRecognitionSystem().dictado(a)

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

            url = str(files("prueba_texto").joinpath(f"{nombre}.txt"))
            FileManager().abrir_archivo(url)

        elif text == "cinco":
            try:
                motor.say("¿que archivo quieres que lea")
                motor.runAndWait()
                nombre = reconocer_voz()
                FileManager().leer_archivo(nombre)

            except FileNotFoundError:
                motor.say("no se encontro el archivo")
                motor.runAndWait()

        elif text == "seis":
            WebNavigator().abrir_google()
            motor.say("google ya esta abierta")
            motor.runAndWait()

        elif text == "siete":
            url = str('C:/Users/Mateo/PycharmProjects/asistem_voice/prueba_texto')
            FileManager().abir_carpeta(url)
            motor.say("La carpeta donde se tiene tus archivos esta abierta")
            motor.runAndWait()

        elif text == "ocho":
            SpeechRecognitionSystem().abrir_calendario()
            motor.say("El calendario esta abierto")
            motor.runAndWait()

        elif text == "nueve":
            motor.say("Elige el numero de la persona a la que deseas enviar el mensaje")
            motor.runAndWait()
            numero: str = reconocer_voz()
            motor.say("Elige el mensaje que deseas enviar")
            motor.runAndWait()


        elif text == "salir":
            motor.say("Hasta luego")
            motor.runAndWait()
            break

        elif text == "repite":
            funciones()

        else:
            motor.say("No se encontró opción")
            motor.runAndWait()
