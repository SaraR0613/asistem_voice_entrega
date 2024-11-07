import tkinter as tk
from tkinter import messagebox
from assistem.modelo import SpeechRecognitionSystem, FileManager, WebNavigator

# Inicializar las clases para acceder a las funciones
speech_system = SpeechRecognitionSystem()
file_manager = FileManager()
web_navigator = WebNavigator()

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Reconocimiento de Voz")
root.geometry("500x600")


# Función para reconocer voz y mostrar el resultado en el Entry de la función seleccionada
def reconocer_voz(entry):
    texto = speech_system.reconocer_voz()
    if texto:
        entry.delete(0, tk.END)
        entry.insert(0, texto)


# Crear funciones para cada botón
def ejecutar_funcion(opcion, entry=None, entry2=None):
    try:
        if opcion == "uno":
            text = entry.get()
            speech_system.dictado(text)
        elif opcion == "dos":
            speech_system.obtener_fecha()
        elif opcion == "tres":
            nombre = entry.get()
            texto = entry2.get()
            file_manager.crear_nota(nombre, texto)
        elif opcion == "cuatro":
            nombre = entry.get()
            file_manager.abrir_archivo(nombre)
        elif opcion == "cinco":
            nombre = entry.get()
            file_manager.leer_archivo(nombre)
        elif opcion == "seis":
            web_navigator.abrir_google()
        elif opcion == "siete":
            url = "C:/Users/Sarita/PycharmProjects/asistem_voice_entrega/prueba_texto"
            file_manager.abir_carpeta(url)
        elif opcion == "ocho":
            speech_system.abrir_calendario()
        elif opcion == "nueve":
            nombre = entry.get()
            mensaje = entry2.get()
            web_navigator.enviar_mensaje(nombre, mensaje)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Crear los botones de la interfaz y los campos para cada opción
options = [
    ("Leer texto en voz alta", "uno"),
    ("Decir la fecha y la hora", "dos"),
    ("Crear archivo de texto", "tres"),
    ("Abrir archivo de texto", "cuatro"),
    ("Leer archivo existente", "cinco"),
    ("Abrir Google", "seis"),
    ("Abrir carpeta de archivos", "siete"),
    ("Abrir calendario", "ocho"),
    ("Enviar mensaje", "nueve")
]

# Generar botones y entradas dinámicamente para cada función
for texto, opcion in options:
    frame = tk.Frame(root)
    frame.pack(pady=10)

    label = tk.Label(frame, text=texto)
    label.grid(row=0, column=0, padx=5)

    entry = tk.Entry(frame)
    entry.grid(row=0, column=1, padx=5)

    # Añadir un segundo campo de entrada para opciones que lo necesiten
    entry2 = None
    if opcion in ["tres", "nueve"]:
        entry2 = tk.Entry(frame)
        entry2.grid(row=1, column=1, padx=5)

    btn_voz = tk.Button(frame, text="Reconocer Voz", command=lambda e=entry: reconocer_voz(e))
    btn_voz.grid(row=0, column=2, padx=5)

    # Si existe un segundo campo de entrada, se envía también a la función
    btn_ejecutar = tk.Button(frame, text="Ejecutar",
                             command=lambda o=opcion, e=entry, e2=entry2: ejecutar_funcion(o, e, e2))
    btn_ejecutar.grid(row=0, column=3, padx=5)

# Ejecución de la interfaz
root.mainloop()
