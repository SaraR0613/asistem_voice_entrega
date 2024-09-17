import speech_recognition as sr
from gtts import gTTS
import os
import sys
import datetime
import requests

# Configura tu clave de API de OpenAI aquí
API_KEY = 'tu_clave_de_api'  # Reemplaza con tu clave de API de OpenAI
CHATGPT_API_URL = 'https://api.openai.com/v1/completions'

def speak(text):
    tts = gTTS(text=text, lang='es')
    tts.save("response.mp3")
    os.system("start response.mp3")  # Para Windows
    # os.system("afplay response.mp3")  # Para macOS
    # os.system("mpg321 response.mp3")  # Para Linux

def open_file(file_path):
    os.startfile(file_path)  # Solo funciona en Windows

def close_application(application_name):
    os.system(f"TASKKILL /F /IM {application_name}.exe")  # Solo funciona en Windows

def save_file():
    # Este es un lugar para manejar la lógica de guardar archivos, dependiendo de la aplicación.
    speak("Función de guardar no implementada completamente.")

def send_message():
    # Aquí puedes integrar con un servicio de mensajería si lo deseas.
    speak("Función de enviar no implementada completamente.")

def read_text():
    speak("Leyendo el texto.")

def dictate_text():
    speak("Dictando texto. Por favor, habla.")

def open_google_tab():
    url = 'https://www.google.com'
    webbrowser.open(url)
    speak("Abriendo Google.")

def connect_chatgpt(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 150
    }
    response = requests.post(CHATGPT_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()['choices'][0]['text'].strip()
        speak(f"ChatGPT dice: {result}")
    else:
        speak("No se pudo conectar con ChatGPT.")

def get_datetime():
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    speak(f"La fecha y hora actual son: {date_time_str}")

def open_notepad():
    os.system('notepad')  # Solo funciona en Windows

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Di algo:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Has dicho: {command}")

        if 'abrir archivo' in command:
            # Aquí deberías pedir el nombre del archivo al usuario
            open_file('ruta_del_archivo.txt')
            speak("Abriendo archivo.")

        elif 'cerrar' in command:
            # Aquí deberías pedir el nombre de la aplicación al usuario
            close_application('nombre_del_programa')
            speak("Cerrando aplicación.")

        elif 'guardar' in command:
            save_file()

        elif 'enviar' in command:
            send_message()

        elif 'leer' in command:
            read_text()

        elif 'dictar' in command:
            dictate_text()

        elif 'abrir pestaña de google' in command:
            open_google_tab()

        elif 'conectar con chat gpt' in command:
            # Aquí deberías pedir el prompt al usuario
            connect_chatgpt('¿Cómo estás?')

        elif 'calendario' in command or 'hora' in command:
            get_datetime()

        elif 'bloc de notas' in command:
            open_notepad()

        else:
            speak("No reconozco ese comando.")

    except sr.UnknownValueError:
        speak("No se pudo entender el audio.")
    except sr.RequestError:
        speak("No se pudo conectar con el servicio de reconocimiento de voz.")

if __name__ == "__main__":
    main()