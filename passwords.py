# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwords.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
import re
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive


num = '0123456789'
string = 'abcdefghijklmnopqrstuvwxyz'
alphanum = '[{(ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789^!?@#$_&*-.abcdefghijklmnopqrstuvwxyz)}]'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1678, 1007)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\qtvenv\qtdes\newPassword\password.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(390, 20, 871, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(48)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(60, 220, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(50, 169, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(1120, 166, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(18)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb1.setGeometry(QtCore.QRect(1220, 241, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.rb1.setFont(font)
        self.rb1.setObjectName("rb1")
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb2.setGeometry(QtCore.QRect(1220, 301, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.rb2.setFont(font)
        self.rb2.setObjectName("rb2")
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb3.setGeometry(QtCore.QRect(1220, 360, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.rb3.setFont(font)
        self.rb3.setObjectName("rb3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(50, 420, 671, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(54, 609, 671, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.textbox2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textbox2.setGeometry(QtCore.QRect(60, 660, 1461, 87))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.textbox2.setFont(font)
        self.textbox2.setObjectName("textbox2")
        self.textbox1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textbox1.setGeometry(QtCore.QRect(60, 470, 1461, 87))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.textbox1.setFont(font)
        self.textbox1.setMidLineWidth(0)
        self.textbox1.setObjectName("textbox1")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.generate())
        self.btn1.setGeometry(QtCore.QRect(100, 570, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clr1())
        self.btn2.setGeometry(QtCore.QRect(760, 570, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.store())
        self.btn3.setGeometry(QtCore.QRect(100, 760, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clr2())
        self.btn4.setGeometry(QtCore.QRect(760, 760, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.find())
        self.btn5.setGeometry(QtCore.QRect(260, 830, 531, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: sys.exit())
        self.pushButton.setGeometry(QtCore.QRect(1510, 880, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1678, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionThemes = QtWidgets.QAction(MainWindow)
        self.actionThemes.setObjectName("actionThemes")
        self.actionBackground = QtWidgets.QAction(MainWindow)
        self.actionBackground.setObjectName("actionBackground")
        self.actionText_Colour = QtWidgets.QAction(MainWindow)
        self.actionText_Colour.setObjectName("actionText_Colour")
        self.actionText_Size = QtWidgets.QAction(MainWindow)
        self.actionText_Size.setObjectName("actionText_Size")
        self.actionVisit_Homepage = QtWidgets.QAction(MainWindow)
        self.actionVisit_Homepage.setObjectName("actionVisit_Homepage")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuView.addAction(self.actionMaximize)
        self.menuSettings.addAction(self.actionThemes)
        self.menuSettings.addAction(self.actionBackground)
        self.menuSettings.addAction(self.actionText_Colour)
        self.menuSettings.addAction(self.actionText_Size)
        self.menuHelp.addAction(self.actionVisit_Homepage)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def generate(self):
        try:
            length = int(self.spinBox.text())
        except Exception:
            self.textbox1.clear()
            self.textbox1.insertPlainText("Enter integer password length!!")
        if self.rb1.isChecked():
            select = num
        elif self.rb2.isChecked():
            select = string
        elif self.rb3.isChecked():
            select = alphanum
        else:
            self.textbox1.clear()
            self.textbox1.insertPlainText("You haven't selected any type of password")
            return
        randpass = []
        if length <1:
            self.textbox1.clear()
            self.textbox1.insertPlainText("Select password length more than zero")
        else:
            for _ in range(1,length+1):
                randpass.append(random.choice(select))
            password = ''.join(randpass)
            self.textbox1.clear()
            self.textbox1.insertPlainText(password)
    def clr1(self):
        self.textbox1.clear()
    def clr2(self):
        self.textbox2.clear()

    def store(self):
        password = self.textbox1.toPlainText()
        if password=='':
            self.textbox1.clear()
            self.textbox1.insertPlainText("Please generate a password first.")
            return
        un=self.textbox2.toPlainText()
        if len(un)>20:
            self.textbox2.clear()
            self.textbox2.insertPlainText("Username too long!!")
        else:
            if un=='':
                self.textbox2.clear()
                self.textbox2.insertPlainText("Without entering a username or key your password won't gets saved!!")
            else:
                done=0
                found=0
                try:
                    with open('passwords.txt','r+') as file:
                        t="username: "+un+' '
                        for line in file:
                            if found==0:
                                if re.search(t,line):
                                    found=1
                                    ask = self.showdialog()
                                    
                    if ask==1024:
                        self.update(t,password)
                        done=1
                    else:
                        self.textbox2.clear()
                        self.textbox2.insertPlainText("Choose another username")
                        done=1
                    if done==0:
                        f=open('passwords.txt','a')
                        text="\nusername: {:30}password: {:<15}".format(un,password)
                        f.write(text)
                        f.close()
                        self.textbox2.insertPlainText("Your password is saved in 'passwords.txt' file in this folder")
                except:
                    f=open('passwords.txt','a')
                    text="\nusername: {:30}password: {:<15}".format(un,password)
                    f.write(text)
                    f.close()
                    self.textbox2.clear()
                    self.textbox2.insertPlainText("Your password is saved in 'passwords.txt' file in this folder")

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        
        msg.setText('This username exists\nDo you want to update password')
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle('Replace username')
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.buttonClicked.connect(msgbtn)

        retval = msg.exec_()
        return retval
            
    def update(self, uname, password):
        lin=''
        rep=''
        with open('passwords.txt','r+') as file:
            l=file.readlines()
        with open('passwords.txt','r+') as file:
            for line in file:
                if re.search(uname,line):
                    res=re.search(r'password: \w.*',line)
                    rep+=res.group(0).split()[1]
                    lin+=line.replace(rep,password)
                    break

        with open('passwords.txt','w') as file:
            d=0
            for lines in l:
                if re.search(uname,lines):
                    d=1
                if d==1:
                    file.write(lin)
                    d=0
                else:
                    file.write(lines)

    
    def find(self):
        un=self.textbox2.toPlainText()
        t="username: "+un+' '
        rep=''
        found=0
        if len(un)<1:
            # self.textbox2.clear()
            self.textbox2.insertPlainText("Write a username to search for passwords")
        else:
            with open ("passwords.txt","r") as file:
                for line in file:
                    if re.search(t,line):
                        # print(line)
                        found=1
                        res=re.search(r'password: .*',line)
            #             print(res)
                        rep+=res.group(0).split()[1]
                        # print(rep)
                        break
            if found==1:
                self.passdialog(rep)
            else:
                self.notFound()

    def passdialog(self, rep):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Your saved password is: {}. You can copy your password from password field.".format(rep))
        self.textbox1.clear()
        self.textbox1.insertPlainText(rep)
        msg.setWindowTitle("Saved Password")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        return retval

    def notFound(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Username not found")
        msg.setWindowTitle("Not Found")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        return retval

    # def upload(self):
    #     gauth = GoogleAuth('settings.yaml')
    #     gauth.LocalWebserverAuth()
    #     drive = GoogleDrive(gauth)
    #     file1 = drive.CreateFile({'title':'Passwords.txt'})
    #     file1.SetContentFile('passwords.txt')
    #     # with open('passwords.txt','r') as file:
    #     #     l=file.readlines()
    #     # for i in l:
    #     #     file1.SetContentString(i)
    #     file1.Upload()
    #     mg=QMessageBox()
    #     mg.setIcon(QMessageBox.Information)
    #     mg.setText("Your file has been uploaded")
    #     mg.setWindowTitle("File Uploaded")
    #     mg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Solutions"))
        self.label1.setText(_translate("MainWindow", "Password Solutions"))
        self.label2.setText(_translate("MainWindow", "Length of Password"))
        self.label3.setText(_translate("MainWindow", "Choose type of Password"))
        self.rb1.setText(_translate("MainWindow", "Numeric"))
        self.rb2.setText(_translate("MainWindow", "Alphabetical"))
        self.rb3.setText(_translate("MainWindow", "AlphaNumeric"))
        self.label4.setText(_translate("MainWindow", "Write a password or generate a random password"))
        self.label5.setText(_translate("MainWindow", "Write a username or key to remember password"))
        self.btn1.setText(_translate("MainWindow", "Generate Password"))
        self.btn2.setText(_translate("MainWindow", "Clear"))
        self.btn3.setText(_translate("MainWindow", "Save"))
        self.btn4.setText(_translate("MainWindow", "Clear"))
        self.btn5.setText(_translate("MainWindow", "Find Password"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionNew.setText(_translate("MainWindow", "New "))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionThemes.setText(_translate("MainWindow", "Themes"))
        self.actionBackground.setText(_translate("MainWindow", "Background"))
        self.actionText_Colour.setText(_translate("MainWindow", "Text Colour"))
        self.actionText_Size.setText(_translate("MainWindow", "Text Size"))
        self.actionVisit_Homepage.setText(_translate("MainWindow", "Visit Homepage"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
