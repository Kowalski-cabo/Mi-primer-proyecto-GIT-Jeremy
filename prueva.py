import tkinter as tk
import time



# Función para iniciar el temporizador
def iniciar_temporizador():
    global comienzo, contador, t_corriendo
    contador = 0
    t_corriendo = True
    comienzo = time.time()
    etiqueta_temporizador.config(text="Tiempo restante: 30 segundos")
    etiqueta_resultado.config(text=f"Clics: {contador}")
    actualizar_temporizador()  # Comienza a actualizar el temporizador

# Función para actualizar la cuenta regresiva
def actualizar_temporizador():
    global comienzo, t_corriendo
    if t_corriendo:
        lapso = time.time() - comienzo
        tiempo_restante = max(30 - int(lapso), 0)  # Calcula el tiempo restante
        
        # Actualiza la etiqueta con el tiempo restante
        etiqueta_temporizador.config(text=f"Tiempo restante: {tiempo_restante} segundos")
        
        # Si hay tiempo restante, actualiza la cuenta regresiva cada segundo
        if tiempo_restante > 0:
            ventana.after(1000, actualizar_temporizador)  # Llama a actualizar_temporizador cada 1000 ms (1 segundo)
        else:
            etiqueta_temporizador.config(text="¡Tiempo agotado!")
            t_corriendo = False  # Detiene el temporizador

# Función para contar clics
def contar_click():
    global contador
    if t_corriendo:
        contador += 1
        etiqueta_resultado.config(text=f"Clics: {contador}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Contador de Clics y Cuenta Regresiva")

#frame contenedor principal
P_frame = tk.Frame(ventana,bg="red")
P_frame.pack(fill=tk.BOTH,expand=True,padx=20,pady=20)

contador = 0
comienzo = None
t_corriendo = False

# Etiqueta para mostrar la cuenta regresiva
etiqueta_temporizador = tk.Label(P_frame, text="Tiempo restante: 30 segundos", font=("Arial", 24),bg="light green")
etiqueta_temporizador.pack(pady=20)

# Etiqueta para mostrar el conteo de clics
etiqueta_resultado = tk.Label(P_frame, text="Clics: 0", font=("Arial", 24),bg="light green")
etiqueta_resultado.pack(pady=20)

# Botón para iniciar el temporizador
boton_iniciar = tk.Button(P_frame, text="Iniciar Temporizador", command=iniciar_temporizador, font=("Arial", 14),bg="light yellow")
boton_iniciar.pack(pady=20)

# Botón para contar clics
boton_click = tk.Button(P_frame, text="¡Clic!", command=contar_click, font=("Arial", 14),bg="light yellow")
boton_click.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
