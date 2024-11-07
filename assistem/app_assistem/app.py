import os
from importlib.resources import files
import pyttsx3
import pyaudio
import json
from vosk import Model, KaldiRecognizer
from assistem.modelo import FileManager, SpeechRecognitionSystem, WebNavigator


motor = pyttsx3.init()
motor.setProperty("rate", 160)
p = pyaudio.PyAudio()

def funciones():
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


if __name__ == "__main__":

    motor.say("Hola como estas, espero que te encuentres bien")
    motor.runAndWait()
    #funciones()
    while True:
        motor.say("te escucho")
        motor.runAndWait()

        text = SpeechRecognitionSystem().reconocer_voz()

        if text == "uno":
            motor.say("¿Qué quieres que te lea?")
            motor.runAndWait()
            a = SpeechRecognitionSystem().reconocer_voz()
            SpeechRecognitionSystem().dictado(a)

        elif text == "dos":
            SpeechRecognitionSystem().obtener_fecha()

        elif text == "tres":
            motor.say("¿Qué nombre quieres que tenga el archivo?")
            motor.runAndWait()
            nombre = SpeechRecognitionSystem().reconocer_voz()

            motor.say(f"¿Qué quieres que contenga el archivo {nombre}?")
            motor.runAndWait()
            texto = SpeechRecognitionSystem().reconocer_voz()

            FileManager().crear_nota(nombre, texto)

        elif text == "cuatro":
            motor.say("¿Qué archivo quieres abrir")
            motor.runAndWait()
            nombre = SpeechRecognitionSystem().reconocer_voz()

            url = str(files("prueba_texto").joinpath(f"{nombre}.txt"))
            FileManager().abrir_archivo(url)

        elif text == "cinco":
            try:
                motor.say("¿que archivo quieres que lea")
                motor.runAndWait()
                nombre = SpeechRecognitionSystem().reconocer_voz()
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
            numero = SpeechRecognitionSystem().reconocer_voz()

            motor.say("Elige el mensaje que deseas enviar")
            motor.runAndWait()
            mensaje = SpeechRecognitionSystem().reconocer_voz()

            WebNavigator().enviar_mensaje(numero, mensaje)

        elif text == "salir":
            motor.say("Hasta luego")
            motor.runAndWait()
            break

        elif text == "repite":
            funciones()

        else:
            motor.say("No se encontró opción")
            motor.runAndWait()
