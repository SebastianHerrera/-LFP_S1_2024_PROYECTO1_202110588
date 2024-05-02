
# Manual Técnico

## Descripción General

El presente manual técnico proporciona información detallada sobre el funcionamiento interno y la estructura del sistema. Incluye explicaciones sobre el análisis léxico y sintáctico, así como detalles sobre la implementación del software.

## Análisis Léxico

El análisis léxico es el proceso mediante el cual se identifican y categorizan los tokens individuales (como palabras clave, identificadores, números, etc.) en el código fuente. En nuestro sistema, utilizamos un enfoque basado en un autómata finito determinista (AFD) para llevar a cabo esta tarea.

### Autómata Finito Determinista (AFD)

El AFD utilizado en el análisis léxico de nuestro sistema se representa gráficamente de la siguiente manera:

```
            +-------------+
            |    Inicio   |
            +------+------+
                   |
                   v
         +------------------+
         |  Estado Inicial  |
         +------------------+
                   |
                   | Letra
                   v
         +------------------+
         |  Estado Palabra  |
         +------------------+
                   |
                   | Espacio
                   v
           +--------------+
           |  Estado Inicio |
           +--------------+
                   |
                   | '/' o '='
                   v
         +------------------+
         |  Estado Comentario  |
         +------------------+
                   |
                   | Caracter no válido
                   v
          +--------------+
          |  Estado Error |
          +--------------+
```

### Tabla de Tokens

A continuación se muestra la tabla de tokens junto con las expresiones regulares que definen cada uno:

| Token               | Expresión Regular                 |
|---------------------|-----------------------------------|
| CREATE_DB           | `CrearBD`                         |
| DELETE_DB           | `EliminarBD`                      |
| CREATE_COLLECTION   | `CrearColeccion`                  |
| DELETE_COLLECTION   | `EliminarColeccion`               |
| INSERT_ONE          | `InsertarUnico`                   |
| UPDATE_ONE          | `ActualizarUnico`                 |
| DELETE_ONE          | `EliminarUnico`                   |
| FIND_ALL            | `BuscarTodo`                      |
| FIND_ONE            | `BuscarUnico`                     |

## Análisis Sintáctico

El análisis sintáctico se encarga de analizar la estructura del código fuente para determinar si cumple con las reglas gramaticales del lenguaje de programación. En nuestro sistema, implementamos un análisis sintáctico básico para validar la sintaxis de las sentencias MongoDB generadas.

S -> SENTENCIA
SENTENCIA -> OPERACION | ERROR
OPERACION -> FUNCION '=' DATOS
FUNCION -> CREATE_DB | DELETE_DB | CREATE_COLLECTION | DELETE_COLLECTION | INSERT_ONE | UPDATE_ONE | DELETE_ONE | FIND_ALL | FIND_ONE
DATOS -> STRING | STRING ',' DATOS | OBJECT | OBJECT ',' DATOS
STRING -> "cadena"
OBJECT -> '{' ATTRIBUTES '}'
ATTRIBUTES -> ATTRIBUTE | ATTRIBUTE ',' ATTRIBUTES | ε
ATTRIBUTE -> STRING ':' VALUE
VALUE -> "cadena" | NUMBER | BOOLEAN | OBJECT | ARRAY
NUMBER -> número
BOOLEAN -> true | false
ARRAY -> '[' ELEMENTS ']'
ELEMENTS -> VALUE | VALUE ',' ELEMENTS | ε


## Conclusiones

El manual técnico proporciona una visión detallada del funcionamiento interno de nuestro sistema, incluyendo los procesos de análisis léxico y sintáctico. Además, se incluyen detalles sobre el autómata finito determinista utilizado en el análisis léxico y la gramática libre de contexto utilizada en el análisis sintáctico.

