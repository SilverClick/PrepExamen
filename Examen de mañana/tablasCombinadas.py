import os


from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()

estiloCuerpoTexto = hojaEstilo["BodyText"]
estiloCuerpoTexto.textColor = Color(0,0,150,1)
elementosDoc = []



datos= [["Arriba\nIzquierda", "", "02", "03", "04"],
         ["", "", "12", "13", "14"],
         ["20", "21", "22", "Abajo\nDerecha", ""],
         ["30", "31", "32", "", ""]
         ]


estilo= [("GRID", (0,0), (-1,-1),1, colors.grey),
        ("BACKGROUND", (0,1), (1,1), colors.lavender),
        ("SPAN", (0, 0), (1, 1)),
        ("INNERGRID", (1,1), (-1,-1), 0.5, colors.lavenderblush),
        ("SPAN", (-2, -2), (-1, -1))
         ]


tabla = Table(data=datos)

tabla.setStyle(estilo)

elementosDoc.append(tabla)

documento = SimpleDocTemplate("ejemploTablasCombinadas.pdf", pagesize = A4)
documento.build(elementosDoc)