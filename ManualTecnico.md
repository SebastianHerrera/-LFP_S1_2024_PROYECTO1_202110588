# Manual Técnico

## Descripción del código

El código proporcionado es un editor HTML básico desarrollado utilizando la biblioteca `tkinter` en Python. Permite abrir archivos de texto, traducir su contenido a HTML y mostrar el HTML generado en una interfaz gráfica. La traducción se realiza según un formato predefinido en el archivo de texto de entrada.

## Componentes principales

El código consta de las siguientes partes principales:

1. **Funciones de traducción**: Estas funciones traducen el contenido del archivo de texto a HTML según ciertas reglas definidas en el código. La función `traducir_a_html` realiza la traducción del texto de entrada al formato HTML, mientras que la función `generar_html` guarda el HTML generado en un archivo y lo abre en un navegador web.

2. **Interfaz gráfica**: Se crea una ventana principal utilizando `tkinter`, con dos cuadros de texto para el archivo de entrada y el HTML generado, respectivamente. También se proporciona un botón para abrir archivos de texto, otro para iniciar la traducción y una etiqueta para cada cuadro de texto.

## Requisitos del sistema

- Python 3.x instalado en el sistema.
- Biblioteca estándar de Python: tkinter.
- El navegador web predeterminado del sistema (se utiliza para abrir el archivo HTML generado).

## Instalación y ejecución

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Ejecuta el script Python proporcionado (`editor_html.py`).
3. La aplicación abrirá una ventana donde podrás abrir archivos de texto, traducir su contenido a HTML y ver el HTML generado.

## Limitaciones conocidas

- El formato del archivo de entrada debe seguir ciertas reglas específicas para que la traducción se realice correctamente. Si el formato no es válido, la aplicación mostrará un mensaje de error.
- La aplicación solo funciona con archivos de texto (*.txt).
- La generación de HTML puede no ser perfecta y puede requerir ajustes manuales dependiendo del contenido del archivo de entrada.
