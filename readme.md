# Generador de constancias

Script de Python 3 para generar constancias utilizando una plantilla como base y un documento de texto con los nombres a planchar cada una las constancias.

_________________

## ¿Qué necesito para poder utilizar este script?

- ### Python 3

  Si utilizas Windows puedes descargarlo de su tienda de aplicaciones [aquí](https://apps.microsoft.com/store/detail/python-39/9P7QFQMJRFP7?hl=en-us&gl=us).  

  Para verificar si tienes Python instalado en tu equipo abre una terminal (En Windows puedes utilizar el ***CMD***) y ejecuta el comando: ```python --version``` Si aparece la versión de python es que ya está instalado en tu sistema. ✅

- ### Plantilla para el certificado en formato PDF

  Utiliza un documento de PDF en tamaño carta y almacenalo en la misma carpeta donde descargues este script.

- ### Documento de texto con los nombres a aparecer en las constancias

  Utiliza un archivo con extensión ***.txt*** que contenga únicamente los nombres que aparecerán en las constnacias, cada nombre debe estar en una línea diferente del documento.  
  Ejemplo:

  ```text
  Mario Armando Marín Barradas
  Melissa Cortéz Herrera
  Juan Ignacio Pérez Durán
  ```

_________________

## ¿Cómo utilizar este script?

¿Ya tienes todo lo necesario para utilizar el script? Ahora sigue estos pasos:

- ### Instala las dependencias del script

  Este script necesita de varios paquetes que debes instalar utilizando Python para que funcione correctamente, los nombres de los paquetes se encuentran en el archivo ***requirements.txt*** de este repositorio.  
  Para instalar las dependencias abre una terminal y ubicate en el directorio donde descargues este script y ejecuta el siguiente comando: `pip install -r requirements.txt`

- ### Modifica las contantes

  El script se encuentra en el documento ***main.py*** de este repositorio, puedes modificar las ***VARIABLES GLOBALES*** en este archivo para configurar lo siguiente:

  | VARIABLE  | ¿Qué hace?  |
  | ----------- | ----------- |
  | CARPETA_ALMACENAJE  | Nombre de la carpeta donde se almacenarán las constancias a generar, debe llevar un **/** al final. |
  | NOMBRE_X | Número de la posición X o la palabra "centrado" Ej: 78 o "centrado"  |
  | NOMBRE_Y | Número de la posición Y |
  | NOMBRE_RGB  | Números entre 0 y 255 Ej: [56, 162, 186]  |
  | NOMBRE_FONT | Nombre de la tipografía a utilizar (Puedes utilizar las siguientes tipografías: Courier, Helvetica, Times-Roman) |
  | NOMBRE_FONT_ARCHIVO | Nombre del archivo a utilizar, debe ser extensión .ttf Ej: OpenSans.ttf (Opcional, utilizalo cuando quieras usar una tipografía en específico) |
  | NOMBRE_FONT_SIZE | Tamaño de la tipografía |
  | FOLIO_INICIAL | Número inicial a utilizar (Se utiliza también para nombrar los certificados a generar) |
  | FOLIO_DIGITS | Número de digitos a mostrar Ej: 3 = 001 |
  | FOLIO_X | Número de la posición X o la palabra "centrado" Ej: 235 o "centrado" |
  | FOLIO_Y | Número de la posición Y |
  | FOLIO_RGB | Números entre 0 y 255 Ej: [56, 162, 186] |
  | FOLIO_FONT | Nombre de la tipografía a utilizar (Puedes utilizar las siguientes tipografías: Courier, Helvetica, Times-Roman) |
  | FOLIO_FONT_ARCHIVO | Nombre del archivo a utilizar, debe ser extensión .ttf Ej: OpenSans.ttf (Opcional, utilizalo cuando quieras usar una tipografía en específico) |
  | FOLIO_FONT_SIZE | Tamaño de la tipografía |

- ### Ejecuta el script

  Si ya ajustaste las variables a tus necesidades ya estás listo para ejecutar este script. En tu terminal recuerda ubicarte en la carpeta donde esté el script descargado.  
  Ejemplo:

  ```shell
  python main.py -t certificado.pdf -n nombres.txt -f FOLIO-EJEMPLO
  ```

  En caso de que exista algún error en la ejecución del scirpt, la terminal te mostrara un mensaje con lo que falló por ejemplo, porque no existe el archivo del certificado o de los nombres o también si la tipografía no está bien configurada en la variables.  
  
  Aparecerá un mensaje de **Finalizado** ✅ en color verde en caso de éxito y tus constancias aparecerán en la carpeta que indicaste en la variable *CARPETA_ALMACENAJE*.
