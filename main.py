import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import webbrowser # Para poder abrir el HTML con Chrome

# Función para traducir el contenido del archivo a HTML

def traducir_a_html(texto_entrada):
    # Analizar el texto de entrada y generar HTML
    html_generado = ""
    try:
        # Buscar el título del encabezado y extraerlo
        inicio_titulo = texto_entrada.find("TituloPagina:\"") + len("TituloPagina:\"")
        fin_titulo = texto_entrada.find("\"", inicio_titulo)
        titulo_pagina = texto_entrada[inicio_titulo:fin_titulo]

        # Incluir el título en el encabezado del HTML generado
        html_generado += f"<!DOCTYPE html>\n<html>\n<head>\n<title>{titulo_pagina}</title>\n</head>\n<body>"

        # Remover espacios innecesarios y saltos de línea
        texto_entrada = texto_entrada.replace("\n", "")

        # Verificar que el texto de entrada comience con "Inicio:{" y termine con "}"
        if not texto_entrada.startswith("Inicio:{") or not texto_entrada.endswith("}"):
            raise ValueError("El formato del archivo de entrada no es válido.")

        # Extraer el contenido del bloque Cuerpo
        inicio_cuerpo = texto_entrada.find("Cuerpo:[") + len("Cuerpo:[")
        fin_cuerpo = texto_entrada.find("]", inicio_cuerpo)
        cuerpo = texto_entrada[inicio_cuerpo:fin_cuerpo]

        # Procesar cada elemento del cuerpo
        elementos = cuerpo.split(",")
        for elemento in elementos:
            if "Titulo:" in elemento:
                inicio_texto = elemento.find("texto:\"") + len("texto:\"")
                fin_texto = elemento.find("\"", inicio_texto)
                texto = elemento[inicio_texto:fin_texto]
                inicio_posicion = elemento.find("posicion:\"") + len("posicion:\"")
                fin_posicion = elemento.find("\"", inicio_posicion)
                posicion = elemento[inicio_posicion:fin_posicion]
                inicio_tamaño = elemento.find("tamaño:\"") + len("tamaño:\"")
                fin_tamaño = elemento.find("\"", inicio_tamaño)
                tamaño = elemento[inicio_tamaño:fin_tamaño]
                inicio_color = elemento.find("color:\"") + len("color:\"")
                fin_color = elemento.find("\"", inicio_color)
                color = elemento[inicio_color:fin_color]
                html_generado += f"<h1 style='text-align:{posicion};font-size:{tamaño};color:{color};'>{texto}</h1>"
            elif "Fondo:" in elemento:
                inicio_color = elemento.find("color:\"") + len("color:\"")
                fin_color = elemento.find("\"", inicio_color)
                color = elemento[inicio_color:fin_color]
                html_generado += f"<body style='background-color:{color};'>"
            elif "Parrafo:" in elemento:
                inicio_texto = elemento.find("texto:\"") + len("texto:\"")
                fin_texto = elemento.find("\"", inicio_texto)
                texto = elemento[inicio_texto:fin_texto]
                inicio_posicion = elemento.find("posicion:\"") + len("posicion:\"")
                fin_posicion = elemento.find("\"", inicio_posicion)
                posicion = elemento[inicio_posicion:fin_posicion]
                html_generado += f"<p style='text-align:{posicion};'>{texto}</p>"
            elif "Texto:" in elemento:
                inicio_fuente = elemento.find("fuente=\"") + len("fuente=\"")
                fin_fuente = elemento.find("\"", inicio_fuente)
                fuente = elemento[inicio_fuente:fin_fuente]
                inicio_color = elemento.find("color=\"") + len("color=\"")
                fin_color = elemento.find("\"", inicio_color)
                color = elemento[inicio_color:fin_color]
                inicio_tamaño = elemento.find("tamaño=\"") + len("tamaño=\"")
                fin_tamaño = elemento.find("\"", inicio_tamaño)
                tamaño = elemento[inicio_tamaño:fin_tamaño]
                html_generado += f"<span style='font-family:{fuente};color:{color};font-size:{tamaño};'>Texto normal.</span>"
            elif "Codigo:" in elemento:
                inicio_texto = elemento.find("texto:\"") + len("texto:\"")
                fin_texto = elemento.find("\"", inicio_texto)
                texto = elemento[inicio_texto:fin_texto]
                inicio_posicion = elemento.find("posicion:\"") + len("posicion:\"")
                fin_posicion = elemento.find("\"", inicio_posicion)
                posicion = elemento[inicio_posicion:fin_posicion]
                html_generado += f"<pre style='text-align:{posicion};'>Muestra el texto con fuente de código de ordenador.</pre>"
            elif "Negrita:" in elemento:
                inicio_texto = elemento.find("texto:\"") + len("texto:\"")
                fin_texto = elemento.find("\"", inicio_texto)
                texto = elemento[inicio_texto:fin_texto]
                html_generado += f"<strong>{texto}</strong>"
            elif "Subrayado:" in elemento:
                inicio_texto = elemento.find("texto:\"") + len("texto:\"")
                fin_texto = elemento.find("\"", inicio_texto)
                texto = elemento[inicio_texto:fin_texto]
                html_generado += f"<u>{texto}</u>"
            elif "Tachado:" in elemento:
                inicio_texto = elemento.find("texto:\"") + len("texto:\"")
                fin_texto = elemento.find("\"", inicio_texto)
                texto = elemento[inicio_texto:fin_texto]
                html_generado += f"<strike>{texto}</strike>"
            elif "Cursiva:" in elemento:
                inicio_texto = elemento.find("texto:\"") + len("texto:\"")
                fin_texto = elemento.find("\"", inicio_texto)
                texto = elemento[inicio_texto:fin_texto]
                html_generado += f"<em>{texto}</em>"
            elif "Salto:" in elemento:
                inicio_cantidad = elemento.find("cantidad:\"") + len("cantidad:\"")
                fin_cantidad = elemento.find("\"", inicio_cantidad)
                cantidad = int(elemento[inicio_cantidad:fin_cantidad])
                html_generado += "<br>" * cantidad
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al traducir a HTML: {str(e)}")
    return html_generado


def generar_html(html_generado, titulo_pagina):
    nombre_archivo = f"{titulo_pagina}.html"
    with open(nombre_archivo, 'w', encoding="utf-8") as file:
        file.write(html_generado)
    messagebox.showinfo("Éxito", f"Archivo HTML '{nombre_archivo}' generado exitosamente.")

    # Abrir el archivo en un navegador web
    webbrowser.open(nombre_archivo)

def generar_html(html_generado, titulo_pagina):
    nombre_archivo = f"{titulo_pagina}.html"
    with open(nombre_archivo, 'w', encoding="utf-8") as file:
        file.write(html_generado)
    messagebox.showinfo("Éxito", f"Archivo HTML '{nombre_archivo}' generado exitosamente.")

    # Abrir el archivo en un navegador web
    webbrowser.open(nombre_archivo)

# Función para abrir un archivo y cargar su contenido en el primer cuadro de texto
def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, 'r', encoding="utf-8") as file:
            contenido = file.read()
            texto_entrada.delete(1.0, tk.END)
            texto_entrada.insert(tk.END, contenido)

# Función para traducir el contenido del primer cuadro de texto a HTML y mostrarlo en el segundo cuadro de texto
def traducir():
    contenido = texto_entrada.get(1.0, tk.END)
    html_generado = traducir_a_html(contenido)
    texto_salida.delete(1.0, tk.END)
    texto_salida.insert(tk.END, html_generado)

    generar_html(html_generado,"HTML_Generado")

    

    


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor HTML")

# Ajustar el tamaño de la ventana
ancho_ventana = 950
alto_ventana = 550
posicion_x = int(ventana.winfo_screenwidth() / 2 - ancho_ventana / 2)
posicion_y = int(ventana.winfo_screenheight() / 2 - alto_ventana / 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

# Cambiar el tema y el estilo de la ventana
ventana.configure(bg="#1E1E1E")

# Estilo para los botones
style = ttk.Style()
style.theme_use('clam')  # Seleccionar un tema para ttk

# Configurar el estilo de los botones
style.configure('TButton', foreground="white", background="#333333", borderwidth=0, focuscolor="#555555")
style.map('TButton', foreground=[('pressed', 'white'), ('active', 'white')], background=[('pressed', '#555555'), ('active', '#555555')])

# Crear los elementos de la interfaz gráfica con estilo personalizado
etiqueta_entrada = tk.Label(ventana, text="Archivo de entrada:", fg="white", bg="#1E1E1E")
etiqueta_entrada.grid(row=0, column=0, padx=10, pady=10)

texto_entrada = tk.Text(ventana, width=60, height=20, bg="#333333", fg="white", insertbackground="white")
texto_entrada.grid(row=1, column=0, padx=10, pady=10)

boton_abrir = ttk.Button(ventana, text="Abrir archivo", command=abrir_archivo)
boton_abrir.grid(row=2, column=0, padx=10, pady=10, sticky="n")

etiqueta_salida = tk.Label(ventana, text="HTML generado:", fg="white", bg="#1E1E1E")
etiqueta_salida.grid(row=0, column=1, padx=10, pady=10)

texto_salida = tk.Text(ventana, width=60, height=20, bg="#333333", fg="white", insertbackground="white")
texto_salida.grid(row=1, column=1, padx=10, pady=10)

boton_traducir = ttk.Button(ventana, text="Traducir", command=traducir)
boton_traducir.grid(row=2, column=1, padx=10, pady=10, sticky="n")

# Ejecutar la aplicación
ventana.mainloop()