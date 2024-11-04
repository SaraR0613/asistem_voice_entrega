import tkinter as tk
from tkinter import messagebox
from assistem.model_asistem import SpeechRecognitionSystem, FileManager, WebNavigator
import threading

# Inicializamos las clases del asistente de voz
asistente = SpeechRecognitionSystem()
gestor_archivos = FileManager()
navegador_web = WebNavigator()


# Función para el reconocimiento de voz y ejecución de comandos
def ejecutar_comando_por_voz():
    from test.tests import reconocer_voz, funciones  # Importamos la función para reconocer la voz
    comando = reconocer_voz()  # Escucha la voz y obtiene el comando en texto

    # Mostramos el comando detectado en la interfaz
    text_output.set(f"Has dicho: {comando}")

    # Ejecutamos la función correspondiente al comando
    if comando == "uno":
        asistente.hablar("¿Qué quieres que te lea?")
        texto_para_leer = reconocer_voz()
        asistente.hablar(texto_para_leer)

    elif comando == "dos":
        asistente.obtener_fecha()

    elif comando == "tres":
        asistente.hablar("¿Qué nombre quieres que tenga el archivo?")
        nombre_archivo = reconocer_voz()
        asistente.hablar(f"¿Qué quieres que contenga el archivo {nombre_archivo}?")
        contenido_archivo = reconocer_voz()
        gestor_archivos.crear_nota(nombre_archivo, contenido_archivo)

    elif comando == "cuatro":
        asistente.hablar("¿Qué archivo quieres abrir?")
        nombre_archivo = reconocer_voz()
        gestor_archivos.abrir_archivo(f"C:/Prueba/{nombre_archivo}.txt")

    elif comando == "cinco":
        asistente.hablar("¿Qué archivo quieres que lea?")
        nombre_archivo = reconocer_voz()
        gestor_archivos.leer_archivo(nombre_archivo)

    elif comando == "seis":
        navegador_web.abrir_google()

    elif comando == "siete":
        gestor_archivos.abir_carpeta("C:/Prueba")

    elif comando == "salir":
        asistente.hablar("Hasta luego")
        root.quit()  # Cierra la interfaz gráfica

    elif comando == "repite":
        funciones()  # Repite las opciones

    else:
        asistente.hablar("No se encontró opción")


# Función para manejar el botón de escucha en un hilo separado
def iniciar_escucha():
    threading.Thread(target=ejecutar_comando_por_voz).start()


# Configuración de la ventana principal
root = tk.Tk()
root.title("Asistente de Voz")
root.geometry("400x200")

# Variable para mostrar el texto de salida
text_output = tk.StringVar()
text_output.set("Presiona 'Escuchar' para iniciar")

# Etiqueta para mostrar los comandos detectados
tk.Label(root, textvariable=text_output, wraplength=350, justify="center").pack(pady=20)

# Botón para iniciar el modo de escucha
tk.Button(root, text="Escuchar", command=iniciar_escucha).pack(pady=20)

# Iniciar la interfaz gráfica
root.mainloop()
