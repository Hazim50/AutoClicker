from PyQt5. QtWidgets import *
from PyQt5. QtCore import *
from PyQt5. QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("AutoClicker")
        #---------
        self.frame1=QFrame(self)
        self.frame1.setGeometry(20, 40, 191, 121)
        self.frame1.setObjectName("frame1")
        self.frame1.setStyleSheet(u"#frame1 { border: 1px solid black; border-color: black}")

        self.button = QPushButton("baslat",self)
        self.button.setGeometry(10, 400, 75, 23)

        self.button2 = QPushButton("durdur",self)
        self.button2.setGeometry(110, 400, 75, 23)

        self.label2=QLabel("Butonlar",self.frame1)
        self.label2.setGeometry(70,10,47,17)

        self.rdbutton1=QRadioButton(self.frame1)
        self.rdbutton1.setText("sol")
        self.rdbutton1.setChecked(True)
        self.rdbutton1.setObjectName("left")
        self.rdbutton1.setGeometry(20,50,61,17)

        self.rdbutton2=QRadioButton(self.frame1)
        self.rdbutton2.setText("orta")
        self.rdbutton2.setObjectName("middle")
        self.rdbutton2.setGeometry(60,80,82,17)

        self.rdbutton3=QRadioButton(self.frame1)
        self.rdbutton3.setText("sağ")
        self.rdbutton3.setObjectName("right")
        self.rdbutton3.setGeometry(110,50,82,17)

        self.buttonGroup=QButtonGroup(self.frame1)
        self.buttonGroup.addButton(self.rdbutton1)
        self.buttonGroup.addButton(self.rdbutton2)
        self.buttonGroup.addButton(self.rdbutton3)

        #--------

        self.frame2=QFrame(self)
        self.frame2.setGeometry(270, 40, 181, 121)
        self.frame2.setObjectName("frame2")
        self.frame2.setStyleSheet(u"#frame2 { border: 1px solid black; border-color: black}")

        self.label3=QLabel(self.frame2)
        self.label3.setText("Tıklama Türü")
        self.label3.setGeometry(50, 10, 131, 16)

        self.rdbutton4=QRadioButton("Tekrar:",self.frame2)
        self.rdbutton4.setObjectName("tekrar")
        self.rdbutton4.setGeometry(10, 50, 91, 17)

        self.rdbutton5=QRadioButton("Sonsuz",self.frame2)
        self.rdbutton5.setObjectName("sonsuz")
        self.rdbutton5.setChecked(True)
        self.rdbutton5.setGeometry(10, 90, 91, 17)

        self.buttonGroup2=QButtonGroup(self.frame2)
        self.buttonGroup2.addButton(self.rdbutton4)
        self.buttonGroup2.addButton(self.rdbutton5)

        self.lineEdit2=QLineEdit(self.frame2)
        self.lineEdit2.setText("100")
        self.lineEdit2.setGeometry(100, 50, 61, 20)

        #---------

        self.frame3=QFrame(self)
        self.frame3.setGeometry(20,180,191,121)
        self.frame3.setObjectName("frame3")
        self.frame3.setStyleSheet(u"#frame3 { border: 1px solid black; border-color: black}")

        self.label4=QLabel("Frekans",self.frame3)
        self.label4.setGeometry(70,0,47,17)

        self.rdbutton6=QRadioButton("Saniye Başı :",self.frame3)
        self.rdbutton6.setObjectName("snBasi")
        self.rdbutton6.setChecked(True)
        self.rdbutton6.setGeometry(10, 30, 82, 17)

        self.rdbutton7=QRadioButton("Gecikme (ms):",self.frame3)
        self.rdbutton7.setObjectName("gecikme")
        self.rdbutton7.setGeometry(10, 60, 82, 17)

        self.buttonGroup3=QButtonGroup(self.frame3)
        self.buttonGroup3.addButton(self.rdbutton6)
        self.buttonGroup3.addButton(self.rdbutton7)

        self.lineEdit3=QLineEdit("1",self.frame3)
        self.lineEdit3.setGeometry(100, 30, 71, 20)

        self.lineEdit4=QLineEdit("1000",self.frame3)
        self.lineEdit4.setGeometry(100, 60, 71, 20)

