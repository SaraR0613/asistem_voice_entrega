from assistem import model_asistem as ma
import pyttsx3
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init()
p = pyaudio.PyAudio()
while True:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    """engine.say("si quieres que te lea algo di uno\n"
               "si quieres que te diga la hora y el dia di dos\n"
               "si quieres abrir una carpeta di tres\n"
               "si quieres abrir un nuevo blog de notas di cuatro\n"
               "si quieres abrir google di cinco")
    engine.runAndWait()"""
    engine.say("habla")
    engine.runAndWait()
    with mic as source:
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language='ES')

    if text == "uno":
        engine.say("que quieres que te lea")
        engine.runAndWait()
        with mic as source:
            audio = recognizer.listen(source)
        a = recognizer.recognize_google(audio, language='ES')
        ma.SpeechRecognitionSystem().speak(a)
    elif text == "dos":
        ma.SpeechRecognitionSystem().get_datetime()
    elif text == "tres":
        url = str("C:/Prueba")
        ma.Fillemanager().open_file(url)
    elif text == "cuatro":
        ma.Fillemanager().open_notepad()
    elif text == "cinco":
        ma.Webnavegartor().open_google_tab()
    elif text == "salir":
        engine.say("Hasta luego")
        engine.runAndWait()
        break
    else:
        engine.say("No se encontro opcion")
        engine.runAndWait()
print(text)
