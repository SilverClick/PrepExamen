import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()

estiloCuerpoTexto = hojaEstilo["BodyText"]
estiloCuerpoTexto2 = hojaEstilo["Heading4"]
estiloCuerpoTexto.textColor = Color(0,0,150,1)
elementosDoc = []

imagen = Image("giu.png")

parragrafo = Paragraph("Optare", style=estiloCuerpoTexto)
parragrafo2 = Paragraph("Optare", style=estiloCuerpoTexto2)

datos = [["Empresas", "Candidato 1", "Candidato 2", "Especificaciones"],
         ["Ayco", "Marcos", "Rubén", "Desenvolvimiento web con PHP"],
         [[parragrafo,parragrafo2], "Borja", "Juan", "Reconocimiento de imagenes con OpenCV"],
         [[parragrafo, imagen], "Lider Supremo Máximo", "Lucas", "Aplicaciones para las Telco"]
         ]

estilo= [("TEXTCOLOR", (0,0), (0,-1), colors.blue),
        ("TEXTCOLOR", (1,0), (-1,0), colors.blueviolet),
        ("TEXTCOLOR", (1,1), (-1,-1), colors.grey),
        ("BOX", (1,1), (-1,-1),1.25, colors.grey),
        ("INNERGRID", (1,1), (-1,-1), 1.25, colors.lightgrey),
        ("VALING", (0,0), (-1,-1), "MIDDLE")
         ]

tabla= Table(data=datos)

tabla.setStyle(estilo)

elementosDoc.append(tabla)

documento = SimpleDocTemplate("ejemploTablasRplCambiada.pdf", pagesize = A4)
documento.build(elementosDoc)