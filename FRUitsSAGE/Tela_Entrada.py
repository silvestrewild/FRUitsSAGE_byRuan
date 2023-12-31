# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Entrada.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from main import beM
import main as be
import Relatorio_Ajuda as raj
from PyQt5 import QtCore, QtGui, QtWidgets


try:
    pont = be.Arquivo_Abrir
except EOFError:
    be.Arquivo_salvar


class BeMDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(BeMDialog, self).__init__(parent)
        self.setWindowTitle("Aguarde...")
        self.setModal(True)

        layout = QtWidgets.QVBoxLayout(self)

        # Adiciona uma QLabel com a mensagem "Carregando..."
        loading_label = QtWidgets.QLabel("Carregando...")
        loading_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        loading_label.setFont(font)
        layout.addWidget(loading_label)

        # Configura um temporizador para fechar o diálogo após 3 segundos (3000 ms)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.fechar_dialogo)
        self.timer.start(3000)

    def fechar_dialogo(self):
        self.timer.stop()  # Pára o temporizador
        self.accept()  # Fecha o diálogo quando o temporizador expira
        self.parent().hide()  # Isso oculta a janela principal
        beM()  # Chama a função beM após fechar o diál

    def abrir_main_window(self):
        self.parent().show()


class Tela_de_Entrada(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 547)
        MainWindow.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 15pt \"Ravie\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 160, 151, 41))
        self.label_2.setObjectName("label_2")
        self.jogar = QtWidgets.QPushButton(self.centralwidget)
        self.jogar.setGeometry(QtCore.QRect(270, 370, 191, 61))
        self.jogar.setStyleSheet("color: rgb(0, 76, 0);\n"
"alternate-background-color: rgb(96, 255, 48);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-color: rgb(85, 170, 0);\n"
"border-color: rgb(0, 170, 0);\n"
"alternate-background-color: rgb(10, 112, 66);\n"
"background-color: rgb(85, 255, 0);\n"
"font: 14pt \"NSimSun\";")
        self.jogar.setObjectName("jogar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 261, 91))
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 15pt \"Ravie\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-10, -60, 711, 601))
        self.label_3.setStyleSheet("\n"
"background-image: url(:/img/fazenda_fundo.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 160, 421, 111))
        self.label.setStyleSheet("font: 18pt \"Ravie\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 470, 93, 28))
        self.pushButton.setStyleSheet("font: 8pt \"NSimSun\";\n"
"background-color: rgb(170, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_3.raise_()
        self.label_2.raise_()
        self.jogar.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionM_sica = QtWidgets.QAction(MainWindow)
        self.actionM_sica.setObjectName("actionM_sica")
        self.actionAjuda = QtWidgets.QAction(MainWindow)
        self.actionAjuda.setObjectName("actionAjuda")

        self.jogar.clicked.connect(self.iniciar_jogo)
        self.pushButton.clicked.connect(raj.app)
        self.MainWindow = MainWindow 

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#005500;\">Bem Vindos</span></p></body></html>"))
        self.jogar.setText(_translate("MainWindow", "JOGAR"))
        self.label_4.setText(_translate("MainWindow", f"Pontuação:{pont()}"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ravie\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; color:#7564de;\">FRU</span><span style=\" font-size:28pt; font-style:italic; color:#647ade;\">its</span><span style=\" font-size:28pt; font-weight:600; color:#de64c3;\">SAGE</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Ajuda"))
        self.actionM_sica.setText(_translate("MainWindow", "Música"))
        self.actionAjuda.setText(_translate("MainWindow", "Ajuda"))

    def iniciar_jogo(self):
        bem_dialog = BeMDialog(self.MainWindow)
        bem_dialog.show()


    def finalizar_beM(self, dialog):
        beM()
        dialog.accept()


import img


if  __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindows = MainWindow
    ui = Tela_de_Entrada()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
