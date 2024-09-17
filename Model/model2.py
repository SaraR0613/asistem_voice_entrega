import speech_recognition as sr
import pyttsx3
import os
import datetime
import requests

# Configura tu clave de API de OpenAI aquí
API_KEY = 'tu_clave_de_api'  # Reemplaza con tu clave de API de OpenAI
CHATGPT_API_URL = 'https://api.openai.com/v1/completions'

# Inicializa el motor de texto a voz
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_file(file_path):
    os.system(f'start {file_path}')  # Solo funciona en Windows
    # Para macOS y Linux, podrías usar open {file_path} o xdg-open {file_path}

def close_application(application_name):
    os.system(f"TASKKILL /F /IM {application_name}.exe")  # Solo funciona en Windows
    # Para macOS y Linux, usa pkill {application_name}

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
    os.system(f'start {url}')  # Solo funciona en Windows
    # Para macOS, usa open {url} y para Linux xdg-open {url}

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
    # Para macOS, podrías usar open -a TextEdit y para Linux gedit o nano

def main():
    pass