import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QStatusBar, \
    qApp, QMenu, QTextEdit, QTabWidget, QWidget, QHBoxLayout, \
    QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt     # ToolButtonTextUnderIcon için
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtCore     # Toolbar default pozisyonları için

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OK')
        self.setGeometry(200,80,1000,600)
        self.UI()
        self.show()

    def UI(self):
        self.mainMenu()
        self.fileMenu()
        self.editMenu()
        self.viewMenu()
        self.toolMenu()
        self.applications()
        self.toolbarMenu()
        self.tabWidgets()
        self.tabText_layout()
        self.tabEksisozluk_layout()

    def mainMenu(self):
        self.menuBar = self.menuBar()
        self.statusBar()
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        # self.tabs.currentChanged.connect(self.tabChanged)

    def fileMenu(self):
        self.file = self.menuBar.addMenu('File')
        ########################################
        self.newAct = QAction(QIcon('icons/mainwindow/filemenu/new.png'), 'New', self)
        self.file.addAction(self.newAct)
        self.openAct = QAction(QIcon('icons/mainwindow/filemenu/open.png'), 'Open', self)
        self.file.addAction(self.openAct)
        self.saveAct = QAction(QIcon('icons/mainwindow/filemenu/save.png'), 'Save', self)
        self.file.addAction(self.saveAct)
        self.saveasAct = QAction('Save as',self)
        self.file.addAction(self.saveasAct)
        self.file.addSeparator()
        self.printAct = QAction(QIcon('icons/mainwindow/filemenu/print.png'), 'Print', self)
        self.file.addAction(self.printAct)
        self.printpreviewAct = QAction(QIcon('icons/mainwindow/filemenu/printpreview.png'),'Print Preview',self)
        self.file.addAction(self.printpreviewAct)
        self.file.addSeparator()
        self.import_sm = QMenu('Import',self)
        self.file.addMenu(self.import_sm)
        self.export_sm = QMenu('Export',self)
        self.file.addMenu(self.export_sm)
        self.importAct = QAction(QIcon('icons/mainwindow/filemenu/import.png'), 'Import', self)
        self.import_sm.addAction(self.importAct)
        self.exportPDFAct = QAction(QIcon('icons/mainwindow/filemenu/exportPDF.png'),'PDF Export',self)
        self.export_sm.addAction(self.exportPDFAct)
        self.exportAct = QAction(QIcon('icons/mainwindow/filemenu/export.png'), 'Export', self)
        self.export_sm.addAction(self.exportAct)
        self.file.addSeparator()
        self.exitAct = QAction(QIcon('icons/mainwindow/filemenu/exit.png'), 'Exit', self)
        self.exitAct.setShortcut('Ctrl+q')         # Uyarı: + nın sağ ve solunda boşluk olmasın
        self.file.addAction(self.exitAct)
        self.exitAct.triggered.connect(qApp.quit)

    def editMenu(self):
        self.edit = self.menuBar.addMenu('Edit')
        ########################################
        self.cutAct = QAction(QIcon('icons/mainwindow/editmenu/cut.png'), 'Cut', self)
        self.edit.addAction(self.cutAct)
        self.copyAct = QAction(QIcon('icons/mainwindow/editmenu/copy.png'), 'Copy', self)
        self.edit.addAction(self.copyAct)
        self.pasteAct = QAction(QIcon('icons/mainwindow/editmenu/paste.png'), 'Paste', self)
        self.edit.addAction(self.pasteAct)
        self.deleteAct = QAction('Delete',self)
        self.edit.addAction(self.deleteAct)
        self.edit.addSeparator()
        self.undoAct = QAction(QIcon('icons/mainwindow/editmenu/undo.png'), 'Undo', self)
        self.undoAct.setShortcut('Ctrl+z')
        self.edit.addAction(self.undoAct)
        self.redoAct = QAction(QIcon('icons/mainwindow/editmenu/redo.png'), 'Redo', self)
        self.redoAct.setShortcut('Ctrl+Shift+z')
        self.edit.addAction(self.redoAct)

    def viewMenu(self):
        self.view = self.menuBar.addMenu('View')
        ########################################
        self.boldAct = QAction(QIcon('icons/mainwindow/viewmenu/textbold.png'),'Bold',self)
        self.view.addAction(self.boldAct)
        self.italicAct = QAction(QIcon('icons/mainwindow/viewmenu/italic.png'),'Italic',self)
        self.view.addAction(self.italicAct)
        self.underlineAct = QAction(QIcon('icons/mainwindow/viewmenu/underline.png'),'Underline',self)
        self.view.addAction(self.underlineAct)
        self.view.addSeparator()
        self.alignleftAct = QAction(QIcon('icons/mainwindow/viewmenu/alignleft.png'),'Align Left',self)
        self.view.addAction(self.alignleftAct)
        self.aligncenterAct = QAction(QIcon('icons/mainwindow/viewmenu/aligncenter.png'),'Align Center',self)
        self.view.addAction(self.aligncenterAct)
        self.alignrightAct = QAction(QIcon('icons/mainwindow/viewmenu/alignright.png'),'Align Right',self)
        self.view.addAction(self.alignrightAct)
        self.alignjustifyAct = QAction(QIcon('icons/mainwindow/viewmenu/alignjustify.png'),'Align Justify',self)
        self.view.addAction(self.alignjustifyAct)
        self.view.addSeparator()
        self.fontAct = QAction(QIcon('icons/mainwindow/viewmenu/font.png'), 'Font', self)
        self.view.addAction(self.fontAct)
        self.colorAct = QAction(QIcon('icons/mainwindow/viewmenu/color.png'), 'Color', self)
        self.view.addAction(self.colorAct)

    def toolMenu(self):
        self.tool = self.menuBar.addMenu('Tool')
        ########################################
        self.showtimeAct = QAction(QIcon('icons/mainwindow/toolmenu/time.png'),'Time',self)
        self.tool.addAction(self.showtimeAct)
        self.showdateAct = QAction(QIcon('icons/mainwindow/toolmenu/date.png'),'Date',self)
        self.tool.addAction(self.showdateAct)

    def applications(self):
        self.apps = self.menuBar.addMenu('Apps')
        ########################################
        self.exchange_currency = QAction(QIcon('icons/apps/exc_currency.png'), 'Exchange', self)
        self.exchange_currency.setShortcut('Ctrl+e')
        self.exchange_currency.setStatusTip('Current currency values from investing.com')
        self.apps.addAction(self.exchange_currency)
        self.eksisozluk = QAction(QIcon('icons/apps/eksisozluk.png'), 'ekşisözlük', self)
        self.eksisozluk.setShortcut('Ctrl+h')
        self.eksisozluk.setStatusTip('Current news from eksisozluk.com')
        self.apps.addAction(self.eksisozluk)

    def toolbarMenu(self):
        tb_width = 50
        self.tb_file = self.addToolBar('File')
        self.tb_file.setFixedWidth(tb_width)
        self.tb_file.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.tb_file)
        self.tb_edit = self.addToolBar('Edit')
        # self.tb_edit.setFixedWidth(tb_width)
        self.tb_edit.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tb_view = self.addToolBar('View')
        # self.tb_view.setFixedWidth(tb_width)
        self.tb_view.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tb_tool = self.addToolBar('Tool')
        # self.tb_tool.setFixedWidth(tb_width)
        self.tb_tool.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tb_apps = self.addToolBar('Useful Apps')
        # self.tb_apps.setFixedWidth(tb_width)
        self.tb_apps.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ######################Toolbar Buttons###################
        ######################File#################
        self.tb_file.addAction(self.newAct)
        self.tb_file.addAction(self.openAct)
        self.tb_file.addAction(self.saveAct)
        self.tb_file.addSeparator()
        self.tb_file.addAction(self.printAct)
        self.tb_file.addAction(self.printpreviewAct)
        self.tb_file.addSeparator()
        self.tb_file.addAction(self.exportPDFAct)
        ######################Edit#################
        self.tb_edit.addAction(self.copyAct)
        self.tb_edit.addAction(self.cutAct)
        self.tb_edit.addAction(self.pasteAct)
        self.tb_edit.addSeparator()
        self.tb_edit.addAction(self.undoAct)
        self.tb_edit.addAction(self.redoAct)
        ######################View#################
        self.tb_view.addAction(self.boldAct)
        self.tb_view.addAction(self.italicAct)
        self.tb_view.addAction(self.underlineAct)
        self.tb_view.addSeparator()
        self.tb_view.addAction(self.alignleftAct)
        self.tb_view.addAction(self.aligncenterAct)
        self.tb_view.addAction(self.alignrightAct)
        self.tb_view.addAction(self.alignjustifyAct)
        self.tb_view.addSeparator()
        self.tb_view.addAction(self.fontAct)
        self.tb_view.addAction(self.colorAct)
        ######################Tool#################
        self.tb_tool.addAction(self.showtimeAct)
        self.tb_tool.addAction(self.showdateAct)
        ######################Exchange Currency#################
        self.tb_apps.addAction(self.exchange_currency)
        self.tb_apps.addAction(self.eksisozluk)

    def tabWidgets(self):
        self.tab_exchange = QWidget()
        self.tab_eksi = QWidget()
        self.tab_text = QWidget()

        self.tabs.addTab(self.tab_exchange, 'Exchange')
        self.tabs.addTab(self.tab_eksi, 'Ekşi Sözlük')
        self.tabs.addTab(self.tab_text,'Text')

    def tabText_layout(self):
        ######################Widgets###################
        self.textedit = QTextEdit()
        self.textedit.setFont(QtGui.QFont('Arial',15))
        ######################Layouts###################
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.textedit)

        self.tab_text.setLayout(self.mainLayout)

    def tabEksisozluk_layout(self):
        ######################Widgets###################
        self.eksisozluk_table = QTableWidget()
        self.eksisozluk_table.setFont(QtGui.QFont('Arial',12))
        ######################Layouts###################
        self.mainLayout_eksi = QHBoxLayout()
        self.mainLayout_eksi.addWidget(self.eksisozluk_table)

        self.tab_eksi.setLayout(self.mainLayout_eksi)



    # def tabChanged(self):
    #     print('Tab changed.')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    app.exit(app.exec_())
