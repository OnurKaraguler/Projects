import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QFontDialog, QColorDialog, \
    QTableWidget, QTableWidgetItem, QHeaderView, QTableView
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
#QFileInfo Pdf export için, Qt alignment için, QTime-> zamanı QDate-> tarihi göstermesi için
from PyQt5.QtCore import QFileInfo,Qt, QTime, QDate
from PyQt5.QtGui import QFont           # yazı kalınlığı gibi (Bold...)
from PyQt5 import QtGui
########################################
from OK_Mainwindow import Mainwindow
from exchange_currency.exchange_app import ExchangeCurrency
# from eksisozluk.eksisozluk_app import Eksisozluk
import eksisozluk.eksisozluk_app as EKSI
########################################

class Functions(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Mainwindow()
        ######################File Menu###################
        self.ui.newAct.triggered.connect(self.fileNew)
        self.ui.openAct.triggered.connect(self.openFile)
        self.ui.saveAct.triggered.connect(self.saveFile)
        self.ui.printAct.triggered.connect(self.printFile)
        self.ui.printpreviewAct.triggered.connect(self.printPreviewDialog)
        self.ui.exportPDFAct.triggered.connect(self.pdfExport)
        ######################Edit Menu###################
        self.ui.copyAct.triggered.connect(self.copyText)
        self.ui.pasteAct.triggered.connect(self.pasteText)
        self.ui.cutAct.triggered.connect(self.cutText)
        self.ui.undoAct.triggered.connect(self.ui.textedit.undo)
        self.ui.redoAct.triggered.connect(self.ui.textedit.redo)
        ######################View Menu###################
        self.ui.boldAct.triggered.connect(self.textBold)
        self.ui.italicAct.triggered.connect(self.textItalic)
        self.ui.underlineAct.triggered.connect(self.textUnderline)
        self.ui.alignleftAct.triggered.connect(self.alignLeft)
        self.ui.aligncenterAct.triggered.connect(self.alignCenter)
        self.ui.alignrightAct.triggered.connect(self.alignRight)
        self.ui.alignjustifyAct.triggered.connect(self.alignJustify)
        self.ui.fontAct.triggered.connect(self.fontDialog)
        self.ui.colorAct.triggered.connect(self.colorDialog)
        ######################Tool Menu###################
        self.ui.showtimeAct.triggered.connect(self.showTime)
        self.ui.showdateAct.triggered.connect(self.showDate)
        ######################App Menu###################
        self.ui.exchange_currency.triggered.connect(self.exchangeCurrencFunk)
        self.ui.eksisozluk.triggered.connect(self.eksisozlukFunk)

    def fileNew(self):
        self.ui.textedit.clear()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '/home')

        if filename[0]:
            self.f = open(filename[0], 'r', encoding='utf-8')

            with self.f:
                self.data = self.f.read()
                self.ui.textedit.setText(self.data)

    def saveFile(self):
        filename = QFileDialog.getSaveFileName(self,'SaveTextFile','/', "Text Files (*.txt)")
        if filename[0]:
            f = open(filename[0], 'w')
            with f:
                text = self.ui.textedit.toPlainText()
                print(text)
                f.write(text)
                QMessageBox.about(self, 'Save File', 'File saved successfully')

    def printFile(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog =QPrintDialog()

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.textedit.print_(printer)

    def printPreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self,printer):
        self.ui.textedit.print_(printer)

    def pdfExport(self):
        fn, _=QFileDialog.getSaveFileName(self,"Export PDF", None, "PDF files (.pdf);;All Files()")

        if fn != '':
            if QFileInfo(fn).suffix() == "" :fn  += '.pdf'

            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.ui.textedit.document().print_(printer)

    def copyText(self):
        cursor = self.ui.textedit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected

    def cutText(self):
        cursor = self.ui.textedit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
        self.ui.textedit.cut()

    def pasteText(self):
        self.ui.textedit.append(self.copiedText)

    def textBold(self):     # todo düzgün çalışmıyor
        font = QFont()
        font.setBold(True)
        self.ui.textedit.setFont(font)

    def textItalic(self):       # todo aynı anda bold, italic ve underline olabilmeli
        font = QFont()
        font.setItalic(True)
        self.ui.textedit.setFont(font)

    def textUnderline(self):
        font = QFont()
        font.setUnderline(True)
        self.ui.textedit.setFont(font)

    def alignLeft(self):
        self.ui.textedit.setAlignment(Qt.AlignLeft)

    def alignCenter(self):
        self.ui.textedit.setAlignment(Qt.AlignCenter)

    def alignRight(self):
        self.ui.textedit.setAlignment(Qt.AlignRight)

    def alignJustify(self):
        self.ui.textedit.setAlignment(Qt.AlignJustify)

    def fontDialog(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.ui.textedit.setFont(font)

    def colorDialog(self):
        cursor = self.ui.textedit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected

        color = QColorDialog.getColor()
        self.ui.textedit.setTextColor(color)

    def showTime(self):
        time = QTime.currentTime()
        self.ui.textedit.setText(time.toString(Qt.DefaultLocaleLongDate))

    def showDate(self):
        date = QDate.currentDate()
        self.ui.textedit.setText(date.toString(Qt.DefaultLocaleLongDate))

    def exchangeCurrencFunk(self):
        self.ui.tabs.setCurrentIndex(0)
        self.exchange_app = ExchangeCurrency()

    def eksisozlukFunk(self):
        self.ui.tabs.setCurrentIndex(1)     # butona basıldığında ilgili tab ın gelmesi

        self.eksisozluk_app = EKSI.eksisozluk()

        # Create table according to the dictionary keys and items
        self.ui.eksisozluk_table.setColumnCount(len(self.eksisozluk_app.keys()))
        hor_Header = []         # HorizontalHeaders List
        for n,key in enumerate(self.eksisozluk_app.keys()):
            hor_Header.append(key)
            self.ui.eksisozluk_table.setRowCount(len(self.eksisozluk_app[key]))
            # Enter data onto Table
            for m, item in enumerate(self.eksisozluk_app[key]):
                newitem = QTableWidgetItem(item)
                self.ui.eksisozluk_table.setItem(m,n, newitem)
            #########################
        self.ui.eksisozluk_table.setHorizontalHeaderLabels(hor_Header)

        # set colums movable
        self.ui.eksisozluk_table.horizontalHeader().setSectionsMovable(True)

        # move a column to another position
        # self.ui.eksisozluk_table.horizontalHeader().swapSections(1, 2)

        # Adjust size of table
        self.ui.eksisozluk_table.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.ui.eksisozluk_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.ui.eksisozluk_table.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        # self.ui.eksisozluk_table.resizeColumnsToContents()
        # self.ui.eksisozluk_table.resizeRowsToContents()

        # reyting değerlerine göre hücrelere renk verme
        nrows = self.ui.eksisozluk_table.rowCount()
        for row in range(0, nrows):
            try:
                item = self.ui.eksisozluk_table.item(row, 1)
                for i in  item.text():
                    if 'b' in i:
                        self.ui.eksisozluk_table.item(row, 0).setBackground(QtGui.QColor('lime'))
                        self.ui.eksisozluk_table.item(row, 1).setBackground(QtGui.QColor('lime'))
                        self.ui.eksisozluk_table.item(row, 2).setBackground(QtGui.QColor('lime'))
                item_text = int(item.text())
                # print(item_text)
                if item_text > 200:
                    self.ui.eksisozluk_table.item(row, 0).setBackground(QtGui.QColor('lime'))
                    self.ui.eksisozluk_table.item(row, 1).setBackground(QtGui.QColor('lime'))
                    self.ui.eksisozluk_table.item(row, 2).setBackground(QtGui.QColor('lime'))
            except:
                continue

        self.ui.eksisozluk_table.setSortingEnabled(True)        # QTableview () gerekli.
        # self.ui.eksisozluk_table.sortItems(1, Qt.DescendingOrder)
        # self.ui.eksisozluk_table.sortByColumn(1, Qt.DescendingOrder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Functions()
    app.exit(app.exec_())