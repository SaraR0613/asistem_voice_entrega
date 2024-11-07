import tkinter as tk
from tkinter import messagebox
import pyttsx3
from importlib.resources import files
import datetime
import os
import pywhatkit
import speech_recognition as sr
from assistem.modelo import SpeechRecognitionSystem

# Configuración del motor de voz
motor = pyttsx3.init()
motor.setProperty("rate", 160)

# Inicialización del reconocedor de voz
recognizer = sr.Recognizer()

# Funciones del asistente
def hablar(texto):
    motor.say(texto)
    motor.runAndWait()

def obtener_fecha():
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    hablar(f"La fecha y hora actual son: {date_time_str}")

def abrir_google():
    url = 'https://www.google.com'
    os.system(f'start {url}')

def crear_nota():
    nombre = nombre_archivo.get()
    texto = contenido_nota.get("1.0", "end-1c")
    with open(str(files("prueba_texto").joinpath(f"{nombre}.txt")), 'w', encoding='utf8') as note:
        note.write(texto)
    messagebox.showinfo("Crear Nota", f"Archivo '{nombre}.txt' creado con éxito.")

def abrir_archivo():
    nombre = nombre_archivo.get()
    url = str(files("prueba_texto").joinpath(f"{nombre}.txt"))
    if os.path.exists(url):
        os.system(f'start {url}')
    else:
        messagebox.showerror("Error", "El archivo no existe")

def leer_archivo():
    nombre = nombre_archivo.get()
    try:
        with open(str(files("prueba_texto").joinpath(f"{nombre}.txt")), 'r', encoding='utf8') as nota:
            contenido = nota.read()
            hablar(contenido)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo no existe")

def abrir_carpeta():
    url = 'C:/Users/Mateo/PycharmProjects/asistem_voice_/prueba_texto'
    if os.path.exists(url):
        os.system(f'start {url}')
    else:
        messagebox.showerror("Error", "La carpeta no existe")

def enviar_mensaje():
    numero = numero_wpp.get()
    mensaje = mensaje_wpp.get()
    hora = int(hora_wpp.get())
    minuto = int(minuto_wpp.get())
    pywhatkit.sendwhatmsg(numero, mensaje, hora, minuto)
    messagebox.showinfo("WhatsApp", "Mensaje programado correctamente.")

def escuchar_y_ingresar(campo):
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            hablar("Por favor, hable ahora.")
            audio = recognizer.listen(source)
            texto = recognizer.recognize_google(audio, language='es-ES')
            campo.delete(0, tk.END) if isinstance(campo, tk.Entry) else campo.delete("1.0", tk.END)
            campo.insert(tk.END, texto)
    except sr.UnknownValueError:
        messagebox.showerror("Error", "No se pudo entender el audio")
    except sr.RequestError:
        messagebox.showerror("Error", "Error con el servicio de reconocimiento de voz")

# Creación de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Asistente de Voz")
ventana.geometry("500x700")

# Creación del Canvas y el Scrollbar
canvas = tk.Canvas(ventana)
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Etiqueta y entrada para el nombre del archivo
tk.Label(scrollable_frame, text="Nombre del archivo:").pack(pady=5)
nombre_archivo = tk.Entry(scrollable_frame)
nombre_archivo.pack(pady=5)
tk.Button(scrollable_frame, text="🎙️", command=lambda: escuchar_y_ingresar(nombre_archivo)).pack(pady=5)
tk.Button(scrollable_frame, text="Ejecutar Crear Nota", command=crear_nota).pack(pady=5)
tk.Button(scrollable_frame, text="Ejecutar Abrir Archivo", command=abrir_archivo).pack(pady=5)
tk.Button(scrollable_frame, text="Ejecutar Leer Archivo", command=leer_archivo).pack(pady=5)

# Área de texto para el contenido de la nota
tk.Label(scrollable_frame, text="Contenido de la nota:").pack(pady=5)
contenido_nota = tk.Text(scrollable_frame, height=5)
contenido_nota.pack(pady=5)
tk.Button(scrollable_frame, text="🎙️", command=lambda: escuchar_y_ingresar(contenido_nota)).pack(pady=5)

# Configuración para mensaje de WhatsApp
tk.Label(scrollable_frame, text="Número de WhatsApp (con código de país):").pack(pady=5)
numero_wpp = tk.Entry(scrollable_frame)
numero_wpp.pack(pady=5)
tk.Button(scrollable_frame, text="🎙️", command=lambda: escuchar_y_ingresar(numero_wpp)).pack(pady=5)

tk.Label(scrollable_frame, text="Mensaje de WhatsApp:").pack(pady=5)
mensaje_wpp = tk.Entry(scrollable_frame)
mensaje_wpp.pack(pady=5)
tk.Button(scrollable_frame, text="🎙️", command=lambda: escuchar_y_ingresar(mensaje_wpp)).pack(pady=5)

tk.Label(scrollable_frame, text="Hora de envío (24h):").pack(pady=5)
hora_wpp = tk.Entry(scrollable_frame)
hora_wpp.pack(pady=5)
tk.Button(scrollable_frame, text="🎙️", command=lambda: escuchar_y_ingresar(hora_wpp)).pack(pady=5)

tk.Label(scrollable_frame, text="Minuto de envío:").pack(pady=5)
minuto_wpp = tk.Entry(scrollable_frame)
minuto_wpp.pack(pady=5)
tk.Button(scrollable_frame, text="🎙️", command=lambda: escuchar_y_ingresar(minuto_wpp)).pack(pady=5)
tk.Button(scrollable_frame, text="Ejecutar Enviar Mensaje WhatsApp", command=enviar_mensaje).pack(pady=5)

# Botones para otras funciones
tk.Button(scrollable_frame, text="Decir la fecha y hora", command=obtener_fecha).pack(pady=5)
tk.Button(scrollable_frame, text="Abrir Google", command=abrir_google).pack(pady=5)
tk.Button(scrollable_frame, text="Abrir Carpeta", command=abrir_carpeta).pack(pady=5)

# Botón de salida
tk.Button(scrollable_frame, text="Salir", command=ventana.quit).pack(pady=20)

# Ejecuta la interfaz
ventana.mainloop()