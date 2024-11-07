import tkinter as tk
from tkinter import messagebox
import pyttsx3
import datetime
import os
import pywhatkit

# Configuración del motor de voz
motor = pyttsx3.init()
motor.setProperty("rate", 160)

# Funciones de las distintas funcionalidades
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
    with open(f'C:/Prueba/{nombre}.txt', 'w', encoding='utf8') as note:
        note.write(texto)
    messagebox.showinfo("Crear Nota", f"Archivo '{nombre}.txt' creado con éxito.")

def abrir_archivo():
    nombre = nombre_archivo.get()
    url = f'C:/Prueba/{nombre}.txt'
    if os.path.exists(url):
        os.system(f'start {url}')
    else:
        messagebox.showerror("Error", "El archivo no existe")

def leer_archivo():
    nombre = nombre_archivo.get()
    try:
        with open(f'C:/Prueba/{nombre}.txt', 'r', encoding='utf8') as nota:
            contenido = nota.read()
            hablar(contenido)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo no existe")

def abrir_carpeta():
    url = "C:/Prueba"
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

# Creación de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Asistente de Voz")
ventana.geometry("500x600")

# Etiqueta y entrada para el nombre del archivo
tk.Label(ventana, text="Nombre del archivo:").pack(pady=5)
nombre_archivo = tk.Entry(ventana)
nombre_archivo.pack(pady=5)

# Área de texto para el contenido de la nota
tk.Label(ventana, text="Contenido de la nota:").pack(pady=5)
contenido_nota = tk.Text(ventana, height=5)
contenido_nota.pack(pady=5)

# Configuración para mensaje de WhatsApp
tk.Label(ventana, text="Número de WhatsApp (con código de país):").pack(pady=5)
numero_wpp = tk.Entry(ventana)
numero_wpp.pack(pady=5)

tk.Label(ventana, text="Mensaje de WhatsApp:").pack(pady=5)
mensaje_wpp = tk.Entry(ventana)
mensaje_wpp.pack(pady=5)

tk.Label(ventana, text="Hora de envío (24h):").pack(pady=5)
hora_wpp = tk.Entry(ventana)
hora_wpp.pack(pady=5)

tk.Label(ventana, text="Minuto de envío:").pack(pady=5)
minuto_wpp = tk.Entry(ventana)
minuto_wpp.pack(pady=5)

# Botones para cada función
tk.Button(ventana, text="Decir la fecha y hora", command=obtener_fecha).pack(pady=5)
tk.Button(ventana, text="Abrir Google", command=abrir_google).pack(pady=5)
tk.Button(ventana, text="Crear Nota", command=crear_nota).pack(pady=5)
tk.Button(ventana, text="Abrir Archivo", command=abrir_archivo).pack(pady=5)
tk.Button(ventana, text="Leer Archivo", command=leer_archivo).pack(pady=5)
tk.Button(ventana, text="Abrir Carpeta", command=abrir_carpeta).pack(pady=5)
tk.Button(ventana, text="Enviar Mensaje WhatsApp", command=enviar_mensaje).pack(pady=5)

# Botón de salida
tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=20)

# Ejecuta la interfaz
ventana.mainloop()


def messagebox():
    return None