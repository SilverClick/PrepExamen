import os

from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.piecharts import Pie, Pie3d

hojaEstilo = getSampleStyleSheet()

elementosDoc = []

temperaturas = [["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciemebre"],
         [15, 16, 20, 25, 27, 31, 35, 38, 30, 25, 20, 18],
         [-3, -4, -1, 4, 6, 9, 12, 15, 16, 10, 2,-2]
         ]

## definimos una area de dibujo
dibujo = Drawing(400,200)

## crear grafico de barras
gb = VerticalBarChart()
## le damos valores al punto x
gb.x =50
## le damos valores al punto y
gb.y =50
gb.height =125
gb.width =350
gb.data = temperaturas[1:]
gb.strokeColor = colors.black
gb.valueAxis._valueMin = -5
gb.valueAxis._valueMax = 40
gb.valueAxis._valueStep = 2
gb.categoryAxis.labels.boxAnchor = "ne"
gb.categoryAxis.labels.dx = 12
gb.categoryAxis.labels.dy = -12
gb.categoryAxis.labels.angle = 30
gb.categoryAxis.categoryNames = temperaturas[0]
gb.groupSpacing = 10
gb.barSpacing = 2

dibujo.add(gb)

elementosDoc.append(dibujo)
elementosDoc.append(Spacer(30,30))


dibujo2 = Drawing(400,200)


gl = HorizontalLineChart()

gl.x =30
gl.y =50
gl.height =125
gl.width =350
gl.data = temperaturas[1:]
## o en ves de lo de arriba
## gl.data = [temperaturas[1]]
gl.categoryAxis.categoryNames = temperaturas[0]
gl.categoryAxis.labels.boxAnchor = "n"
gl.categoryAxis.labels.angle = 30
gl.categoryAxis.labels.dx = 0
gl.categoryAxis.labels.dy = -20
gl.valueAxis._valueMin = -5
gl.valueAxis._valueMax = 40
gl.valueAxis._valueStep = 10
gl.strokeColor = colors.black
gl.lines [0].strokeWidth = 2
gl.lines [0].symbol = makeMarker("FilledCircle")
gl.lines [1].strokeWidth = 1.5


dibujo2.add(gl)



leyenda = LineLegend()
leyenda.fontSize = 8
leyenda.fontName = "Helvetica"
leyenda.alignment = "right"
leyenda.x = 0
leyenda.y = 0
leyenda.columnMaximum = 2
series = ["Máximas", "Minimas"]
leyenda.colorNamePairs = [(gl.lines[i].strokeColor, series[i]) for i in range(len(gl.data))]
# [("red", "Máximas"), ("green", "Minimas")]
dibujo2.add(leyenda)

elementosDoc.append(dibujo2)

elementosDoc.append(Spacer(30,30))

dibujoPie = Drawing(300,200)

tarta = Pie3d()
tarta.x = 65
tarta.y = 15
tarta.data = [10,5,20,25,40]
tarta.labels = ["Edge", "Brave", "Firefox", "Safari", "Chrome"]

tarta.slices.strokeWidth = 0.5

tarta.slices[3].popout = 10
tarta.slices[3].strokeWidth = 2
tarta.slices[3].strokeDashArray = [2,2]
tarta.slices[3].fontColor = colors.blue
tarta.sideLabels = 1


dibujoPie.add(tarta)


leyendaPie = Legend()
leyendaPie.x = 300
leyendaPie.y = 5
leyendaPie.dx = 10
leyendaPie.dy = 10
leyendaPie.fontName = "Helvetica"
leyendaPie.fontSize = 8
leyendaPie.boxAnchor = "n"
leyendaPie.columnMaximum = 15
leyendaPie.strokeWidth = 0.5
leyendaPie.strokeColor = colors.grey
leyendaPie.yGap = 1
leyendaPie.dxTextSpace = 3
leyendaPie.alignment = "right"
leyendaPie.dividerLines = 1|2|3
leyendaPie.dividerOffsY = 4.5
leyendaPie.subCols.rpad = 30

dibujoPie.add(leyendaPie)

paresColoresLeyenda = list()
colores = [colors.blue, colors.red, colors.pink, colors.yellow, colors.green]
for i, color in enumerate(colores):
    tarta.slices[i].fillColor = color
    paresColoresLeyenda.append((color,tarta.labels[i]))


elementosDoc.append(dibujoPie)

documento = SimpleDocTemplate("ejemploGraficasRpl.pdf", pagesize=A4)
documento.build(elementosDoc)