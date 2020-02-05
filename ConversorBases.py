# coding=utf-8
import sys
import string
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "conversorBases.ui"  # Enter file here. extension '.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class ConversorBases(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self, flags = QtCore.Qt.FramelessWindowHint) # Sin Frame
        #QtGui.QMainWindow.__init__(self) # Con Frame
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.pbCalcular.clicked.connect(self.pbClickEvent)
        self.pbQuit.clicked.connect(self.pbQuitEvent)
        self.pbReset.clicked.connect(self.pbResetEvent)

        pal = QtGui.QPalette()
        brush = QtGui.QBrush(QtCore.Qt.white, QtGui.QPixmap('back.jpg'))
        pal.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        pal.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.setPalette(pal)

        self.setFixedSize(629, 363)

    def mousepressevent(self, event):
        self.offset = event.pos()

    def mousemoveevent(self, event):
        x = event.globalx()
        y = event.globaly()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

    def pbQuitEvent(self):
        self.close()

    def pbResetEvent(self):
        self.txtBase.setText("")
        self.txtBaseDest.setText("")
        self.txtResultado.setText("")
        self.txtNumero.setText("")
        self.txtInstrucciones.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'>*** Introduce el n&uacute;mero a cambiar de base; posteriormente, la base del n&uacute;mero::</span></p><p style='margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style=' font-family:Courier New; font-size:10pt; color:#ffffff;'>** Para Hexadecimal &gt; 16</span></p><p style='margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style=' font-family:Courier New; font-size:10pt; color:#ffffff;'>** Para Binario 	&gt; 2</span></p><p style='margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style=' font-family:Courier New; font-size:10pt; color:#ffffff;'>** Para decimal 	&gt; 10</span></p>")

    def pbClickEvent(self):
        pbSender = self.sender()
        Result = self.txtResultado
        instru = self.txtInstrucciones
        # Can use .append(), .setText(), .insertPlainText() to manipulate text in an editText. Try .setHtml() to manipulate Html. :v
        if self.txtBase.text() == '' or self.txtNumero.text() == '':
            instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'>No puede dejar vac&iacute;os los campos!!\n</span></p>")
            return
        numero = self.txtNumero.text()
        base = int(self.txtBase.text())
        toBase = int(self.txtBaseDest.text())
        if base == 10:
            lista = list(range(0, 9 + 1))
            numLista = list(str(numero))
            for cadaNum in numLista:
                if self.tieneLetras(numero):
                    instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'>El numero no coincide con la base indicada!!</span></p>")
                    return
                if int(cadaNum) not in lista and self.tieneLetras(numero):
                    instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'>El numero no coincide con la base indicada!!</span></p>")
                    return
        elif base == 2:
            lista = list(range(0, 1 + 1))
            numLista = list(str(numero))
            for cadaNum in numLista:
                if self.tieneLetras(numero):
                    instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'>El numero no coincide con la base indicada!!</span></p>")
                    return
                if int(cadaNum) not in lista:
                    instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'>El numero no coincide con la base indicada!!</span></p>")
                    return
        elif base == 16:
            lista = list(range(0, 9 + 1))
            numLista = list(str(numero))
            letras = self.tieneLetras(str(numero))
            elemento = ''
            for cada in lista:
                parte = str(cada)
                elemento += parte
            nuevaLista = list(elemento)
            lista = list(nuevaLista)
            for cadaNum in numLista:
                if cadaNum not in lista and letras != True:
                    instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'>El numero no coincide con la base indicada!!</span></p>")
                    return
        else:
            instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'>Escriba una base v&aacute;lida!!</span></p>")
        resultado = self.convert(numero, base, toBase)
        newhtml = "<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'>"
        newhtml = newhtml + "<span style='font-family:Courier New; font-size:10pt; color:#000000;'> %s" % resultado + " </span></p>"
        Result.setHtml(newhtml)

    def letAnum(self, baseRef, let):
        lista = list(let)
        num = ''
        for let in lista:
            if baseRef == 16 and let == 'A':
                let = 10
            elif baseRef == 16 and let == 'B':
                let = 11
            elif baseRef == 16 and let == 'C':
                let = 12
            elif baseRef == 16 and let == 'D':
                let = 13
            elif baseRef == 16 and let == 'E':
                let = 14
            elif baseRef == 16 and let == 'F':
                let = 15
            num += str(let)
        return num

    def tieneLetras(self, numeroString):
        letrasM = list(string.ascii_uppercase[:6])
        letrasm = list(string.ascii_lowercase[:6])
        lista = list(numeroString)
        for eachItem in lista:
            if eachItem in letrasM or eachItem in letrasm:
                return True

    def evaluador_hexa(self, baseH, numero):
        if baseH == 16 and self.tieneLetras(str(numero)):
            return numero
        if baseH == 16 and int(numero) == 10:
            numero = 'A'
        elif baseH == 16 and int(numero) == 11:
            numero = 'B'
        elif baseH == 16 and int(numero) == 12:
            numero = 'C'
        elif baseH == 16 and int(numero) == 13:
            numero = 'D'
        elif baseH == 16 and int(numero) == 14:
            numero = 'E'
        elif baseH == 16 and int(numero) == 15:
            numero = 'F'
        return numero

    def cambio_base(self, decimal, base):
        conversion = ''
        while decimal // base != 0:
            conversion = str(self.evaluador_hexa(base, decimal % base)) + conversion
            conversion = self.evaluador_hexa(base, conversion)
            decimal = decimal // base
        return str(self.evaluador_hexa(base, decimal)) + conversion

    def convert(self, deNum, deBase, aBase):
        aNum = 0
        potencia = 0
        instru = self.txtInstrucciones
        if deBase == aBase:
            instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'> Bases iguales. Resulatdo: %s"%deNum +"</span></p>")
        elif deBase == 10:
            if aBase != 10 and aBase != 2 and aBase != 16:
                instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'> La base de destino no es valida! Intente de nuevo!::\n\n </span></p>")
            return self.cambio_base(int(deNum), aBase)
        elif deBase == 2:
            if aBase != 10 and aBase != 2 and aBase != 16:
                instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'> La base de destino no es valida! </span></p>")
            toBase = aBase
            aBase = 10
            deNum = int(deNum)
            while deNum > 0:
                aNum += deBase**potencia * (deNum % aBase)
                deNum //= aBase
                potencia += 1
            if toBase == aBase:
                return aNum
            else:
                return self.cambio_base(aNum, toBase)
        elif deBase == 16:
            if aBase != 10 and aBase != 2 and aBase != 16:
                instru.setHtml("<p style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style='font-family:Courier New; font-size:10pt; color:#ffffff;'> La base de destino no es valida! Intente de nuevo!::\n\n </span></p>")
            toBase = aBase
            aBase = 10
            deNum = reversed(list(deNum))
            fromNum = deNum
            res = 0
            potencia = 0
            for num in fromNum:
                res += int(self.letAnum(deBase, num))*(deBase**potencia)
                potencia += 1
            if toBase == aBase:
                return res
            else:
                return self.cambio_base(res, toBase)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = ConversorBases()
    window.show()
    sys.exit(app.exec_())
