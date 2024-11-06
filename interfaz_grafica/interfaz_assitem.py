import tkinter as tk
from tkinter import messagebox
from assistem.modelo import FileManager, SpeechRecognitionSystem, WebNavigator
from assistem.app_assistem.app import reconocer_voz


class VoiceAssistantUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente de Voz")
        self.root.geometry("400x200")

        # Estado de la aplicación
        self.label_status = tk.Label(root, text="Bienvenido al Asistente de Voz", font=("Arial", 12))
        self.label_status.pack(pady=20)

        # Botón para activar la escucha
        self.button_listen = tk.Button(root, text="Activar Asistente", command=self.activate_assistant,
                                       font=("Arial", 10))
        self.button_listen.pack(pady=10)

    def activate_assistant(self):
        self.label_status.config(text="Escuchando...")
        self.root.update()
        user_input = reconocer_voz()

        if user_input:
            self.process_command(user_input)
        else:
            self.label_status.config(text="No se entendió, intenta de nuevo.")

    def process_command(self, command):
        if command == "uno":
            SpeechRecognitionSystem().hablar("Dime qué quieres que lea.")
        elif command == "dos":
            SpeechRecognitionSystem().obtener_fecha()
        elif command == "tres":
            SpeechRecognitionSystem().hablar("Dime el nombre del archivo.")
            nombre = reconocer_voz()
            SpeechRecognitionSystem().hablar("¿Qué quieres que contenga el archivo?")
            texto = reconocer_voz()
            FileManager().crear_nota(nombre, texto)
        elif command == "cuatro":
            SpeechRecognitionSystem().hablar("Dime el nombre del archivo a abrir.")
            nombre = reconocer_voz()
            FileManager().abrir_archivo(f"../prueba_texto/{nombre}.txt")
        elif command == "cinco":
            WebNavigator().abrir_google()
        elif command == "salir":
            self.root.quit()
        else:
            self.label_status.config(text="Comando no reconocido, intenta de nuevo.")


# Inicialización de la interfaz
root = tk.Tk()
app = VoiceAssistantUI(root)
root.mainloop()
