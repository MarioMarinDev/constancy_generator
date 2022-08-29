# -*- coding: utf-8 -*-

"""
  [ PAQUETES ]
"""
import argparse
import io
import pathlib
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfbase.pdfmetrics import stringWidth, registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from os.path import exists
from os import mkdir
from termcolor import colored

"""
  [ VARIABLES GLOBALES ]
"""
# Principal
CARPETA_ALMACENAJE = "constancias/"
# Nombre del alumno
NOMBRE_X = 78
NOMBRE_Y = 337
NOMBRE_RGB = [255, 0, 0] # Números entre 0 y 255
NOMBRE_FONT = "Helvetica"
NOMBRE_FONT_ARCHIVO = ""
NOMBRE_FONT_SIZE = 30
# Folio
FOLIO_INICIAL = 1
folio_actual = FOLIO_INICIAL
FOLIO_ZEROS = 0
FOLIO_X = 0
FOLIO_Y = 0
FOLIO_RGB = [0, 0, 0] # Números entre 0 y 255
FOLIO_FONT = "Helvetica"
FOLIO_FONT_ARCHIVO = ""
FOLIO_FONT_SIZE = 10

""" 
 [ FUNCIONES ]
"""
# Mostrar un error
def show_error(message="Desconocido"):
  print(colored("Error: " + message, "red"))

# Validación de datos
def validate_flags(args):
  # Verifica si existe la plantilla de certificado
  if not args.template or not exists(args.template):
    show_error("La plantilla de certificado no existe o no fué asignada.")
    return False
  # Verifica que la plantilla de certificado de un PDF
  if pathlib.Path(args.template).suffix != ".pdf":
    show_error("La plantilla de certificado debe ser un PDF.")
    return False
  # Verifica si existe el archivo de nombres
  if not args.names or not exists(args.names):
    show_error("El documento de texto de nombres no exists o no fué asingado.")
    return False
  return True

# Validación de carpeta de almacenaje
def validate_save_location():
  if not exists(CARPETA_ALMACENAJE):
    mkdir(CARPETA_ALMACENAJE)  

# Crear y guardar constancia
def create_constancy(args, name=""):
  global folio_actual
  # Leer plantilla de certificado
  template = PdfFileReader(open(args.template, "rb"))
  packet = io.BytesIO()
  # Crear pdf a planchar en la plantilla
  canvas = Canvas(packet, pagesize=letter)
  # Configurar texto del nombre
  color = Color(NOMBRE_RGB[0], NOMBRE_RGB[1], NOMBRE_RGB[2])
  if type(NOMBRE_FONT_ARCHIVO) == str and exists(NOMBRE_FONT_ARCHIVO):
    registerFont(TTFont(NOMBRE_FONT, NOMBRE_FONT_ARCHIVO))
  canvas.setFillColor(color)
  try:
    canvas.setFont(NOMBRE_FONT, NOMBRE_FONT_SIZE)
  except:
    show_error("Tipografía de nombre inválida.")
    exit()
  # Planchar nombre del estudiante
  canvas.drawString(NOMBRE_X, NOMBRE_Y, name)
  # Chechar si es necesario planchar folio
  if args.folio:
    folio = args.folio + "-" + str(folio_actual).zfill(FOLIO_ZEROS)
    # Configurar folio a planchar en la plantilla
    color = Color(FOLIO_RGB[0], FOLIO_RGB[1], FOLIO_RGB[2])
    if type(FOLIO_FONT_ARCHIVO) == str and exists(FOLIO_FONT_ARCHIVO):
      registerFont(TTFont(FOLIO_FONT, FOLIO_FONT_ARCHIVO))
    canvas.setFillColor(color)
    try:
      canvas.setFont(FOLIO_FONT, FOLIO_FONT_SIZE)
    except:
      show_error("Tipografía de folio inválida.")
      exit()
    # Planchar folio
    canvas.drawString(FOLIO_X, FOLIO_Y, folio)
    folio_actual += 1
  # Guardar cambios
  canvas.save()
  packet.seek(0)
  canvas_pdf = PdfFileReader(packet)
  # Planchar datos en plantilla
  page = template.getPage(0)
  page.mergePage(canvas_pdf.getPage(0))
  # Crear nuevo PDF de resutlado
  new_pdf = PdfFileWriter()
  new_pdf.addPage(page)
  # Asignar nombre de archivo y locación de almacenaje
  validate_save_location()
  save_location = CARPETA_ALMACENAJE
  if args.folio: save_location += folio
  else: save_location += str(folio_actual)
  save_location += ".pdf"
  # Guardar PDF de resultado
  output = open(save_location, "wb")
  new_pdf.write(output)
  output.close()

"""
  [ PROGRAMA PRINCIPAL ]
"""
print(colored("Generador de constancias de Mario Marín :)", "white", attrs=["bold"]))
# Crear instancia de parser y configuración
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--template", dest="template",  help="Plantilla del certificado en formato PDF")
parser.add_argument("-n", "--names",    dest="names",     help="Documento de texto con los nombres de los estudiantes")
parser.add_argument("-f", "--folio",    dest="folio",     help="Folio a utilizar (Opcional)")

# Obtener argumentos del usuario y validar
args = parser.parse_args()
validated = validate_flags(args)
if not validated: exit()

# Obtener cada uno de los nombres
with open(args.names, "r", encoding="utf-8") as names_file:
  names = names_file.read().split("\n")
  
# Validar cantidad de nombres
if len(names) <= 0 or (len(names) == 1 and names[0] == ""):
  show_error("No hay nombres en el documento de nombres.")
  exit()
  
# Crear constancias por cada nombre en el documento
for name in names:
  create_constancy(args, name)
  
print(colored("¡Finalizado! :D", "green"))
