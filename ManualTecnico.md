# Manual Técnico

## Descripción del código

El código proporcionado es un editor HTML desarrollado en Python utilizando la biblioteca `tkinter`. Su funcionalidad principal es permitir a los usuarios abrir archivos de texto, traducir su contenido a HTML y visualizar el HTML generado en una interfaz gráfica de usuario. La traducción se realiza conforme a un formato predefinido en el archivo de texto de entrada.

## Componentes principales

El código se compone de los siguientes elementos clave:

1. **Funciones de traducción**: Estas funciones son responsables de traducir el contenido del archivo de texto a HTML según ciertas reglas definidas en el código. La función `traducir_a_html` lleva a cabo la traducción del texto de entrada al formato HTML, mientras que la función `generar_html` se encarga de guardar el HTML generado en un archivo y abrirlo en un navegador web. <br> ![Generar HTML](https://github.com/SebastianHerrera/-LFP_S1_2024_PROYECTO1_202110588/blob/main/Imgs/generar_a_html.png) <br> ![Generar HTML](https://github.com/SebastianHerrera/-LFP_S1_2024_PROYECTO1_202110588/blob/main/Imgs/generar_a_html.png)

                                         

2. **Interfaz gráfica de usuario**: Se crea una ventana principal utilizando `tkinter`, la cual incluye dos cuadros de texto: uno para el archivo de entrada y otro para el HTML generado. Además, se proporcionan botones para abrir archivos de texto, iniciar la traducción y etiquetas para cada cuadro de texto.

![Tkinter](https://github.com/SebastianHerrera/-LFP_S1_2024_PROYECTO1_202110588/blob/main/Imgs/tkinter.png)


## Requisitos del sistema

- Python 3.x instalado en el sistema.
- Biblioteca estándar de Python: tkinter.
- Navegador web predeterminado del sistema (se utiliza para abrir el archivo HTML generado).

## Instalación y ejecución

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Ejecuta el script Python proporcionado (`editor_html.py`).
3. La aplicación abrirá una ventana donde podrás abrir archivos de texto, traducir su contenido a HTML y ver el HTML generado.

## Limitaciones conocidas

- El formato del archivo de entrada debe seguir ciertas reglas específicas para que la traducción se realice correctamente. Si el formato no es válido, la aplicación mostrará un mensaje de error.
- La aplicación solo funciona con archivos de texto (*.txt).
- La generación de HTML puede no ser perfecta y puede requerir ajustes manuales dependiendo del contenido del archivo de entrada.

## Arquitectura del código

El código sigue una arquitectura modular, dividiendo la funcionalidad en funciones y componentes reutilizables para una fácil mantenibilidad y extensión en el futuro. Las funciones de traducción están separadas de la interfaz gráfica de usuario, lo que facilita la comprensión del flujo de datos y la depuración.

## Mejoras futuras

- Implementación de una validación más robusta del formato del archivo de entrada para detectar y manejar errores con mayor precisión.
- Adición de opciones de personalización para los estilos de HTML generados, permitiendo a los usuarios ajustar el aspecto final del documento según sus necesidades.
- Incorporación de funcionalidades avanzadas de edición de HTML, como resaltado de sintaxis, autocompletado y vista previa en tiempo real.

Con esta información, los desarrolladores pueden comprender mejor la estructura y el funcionamiento del Editor HTML y realizar futuras mejoras y modificaciones de manera más eficiente.
