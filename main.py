# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from mainwindow import Ui_MainWindow
from Utilisateur import Utilisateur
from Bot import Bot
<<<<<<< HEAD
from PyQt5 import QtSql, QtWidgets
from PyQt5.QtSql import QSqlDatabase
import MySQLdb as mdb
=======
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
>>>>>>> b554d1d6ec443680e059447228a471572214b01a

class Chat(QtWidgets.QMainWindow):
    def __init__(self, title = "Default", parent = None):
        super(Chat, self).__init__(parent)
        """Construteur de la classe"""
        self.main = QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.utilisateur = Utilisateur()
        self.bot = Bot()
        self.ui.setupUi(self)
        self._initSlotButton()
        self.connectDB()

        
        
        
    def connectDB(self):
        """Connection à la base de donnée Local"""
        try : 
            db = mdb.connect('localhost', 'root', 'root', 'chatbot')
            QMessageBox.about(self, 'Connextion', 'Successfully Connected to db')
        except mdb.Error as e :
            QMessageBox.about(self, 'Connextion', 'Not Connected Successfully')
            sys.exit(1)
        


        
        
        
        
    def _initSlotButton (self):
        """Initialise les Slots"""

        self.ui.envoyer.clicked.connect(self.Envoyer)
        self.ui.textUtilisateur.returnPressed.connect(self.Envoyer)

    def Envoyer(self):
        """Envoie le message taper par l'utilisateur"""

        self.msg =self.utilisateur.name + " : " + self.ui.textUtilisateur.text()
        self.ui.textEdit.setAlignment(Qt.AlignRight)
        self.ui.textEdit.append(self.msg)
        self.ui.textEdit.append("")
        self.ui.textUtilisateur.clear()
        self.ui.textEdit.setAlignment(Qt.AlignLeft)
        self.respondBot()



    def respondBot(self):
        """ Envoi la réponsse du bot en fonction de la demande de l'utilisateur"""
        rsp = self.bot.name + " : "

        self.msg = self.msg.lower()

        if self.grosmots()==True:
            rsp += "Surveille ton langage"
        elif "bonjour" in self.msg:
            rsp += "Bonjour comment ça va ?"
        elif "maths" in self.msg:
            rsp += "Voici les exos de maths !"
            self.image()
        else:
            rsp += " Je ne comprend pas !"
        
        self.ui.textEdit.append(rsp)
        self.ui.textEdit.append("")

    
    def grosmots(self):
        grm = ['girafe', 'tigre', 'singe', 'souris']
        for f in grm:
            if f in self.msg:
                return True
        return False
        

    def image(self):
        """Permet de Charger une image

            En Cours de dévellopppement !!!

        """
        self.img = self.ui.textEdit.toHtml() + "<img src = \"../img/maths.png\" alt =\"\"/>"
        self.ui.textEdit.setHtml(self.img)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Chat()
    w.show()
    sys.exit(app.exec_())

        


