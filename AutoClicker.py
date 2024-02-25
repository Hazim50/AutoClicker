from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QLabel, QRadioButton, QButtonGroup, QLineEdit
import sys
import threading
import time
import mouse
from pynput import keyboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("AutoClicker")
        # ---------
        self.frame1 = QFrame(self)
        self.frame1.setGeometry(20, 40, 191, 121)
        self.frame1.setObjectName("frame1")
        self.frame1.setStyleSheet(u"#frame1 { border: 1px solid black; border-color: black}")

        self.button = QPushButton("Start", self)
        self.button.setGeometry(10, 400, 75, 23)

        self.button2 = QPushButton("Stop", self)
        self.button2.setGeometry(110, 400, 75, 23)

        self.label2 = QLabel("Buttons", self.frame1)
        self.label2.setGeometry(70, 10, 47, 17)

        self.rdbutton1 = QRadioButton(self.frame1)
        self.rdbutton1.setText("Left")
        self.rdbutton1.setChecked(True)
        self.rdbutton1.setObjectName("left")
        self.rdbutton1.setGeometry(20, 50, 61, 17)

        self.rdbutton2 = QRadioButton(self.frame1)
        self.rdbutton2.setText("Middle")
        self.rdbutton2.setObjectName("middle")
        self.rdbutton2.setGeometry(60, 80, 82, 17)

        self.rdbutton3 = QRadioButton(self.frame1)
        self.rdbutton3.setText("Right")
        self.rdbutton3.setObjectName("right")
        self.rdbutton3.setGeometry(110, 50, 82, 17)

        self.buttonGroup = QButtonGroup(self.frame1)
        self.buttonGroup.addButton(self.rdbutton1)
        self.buttonGroup.addButton(self.rdbutton2)
        self.buttonGroup.addButton(self.rdbutton3)

        # --------

        self.frame2 = QFrame(self)
        self.frame2.setGeometry(270, 40, 181, 121)
        self.frame2.setObjectName("frame2")
        self.frame2.setStyleSheet(u"#frame2 { border: 1px solid black; border-color: black}")

        self.label3 = QLabel(self.frame2)
        self.label3.setText("Click Type")
        self.label3.setGeometry(65, 10, 131, 16)

        self.rdbutton4 = QRadioButton("repeat:", self.frame2)
        self.rdbutton4.setObjectName("repeat")
        self.rdbutton4.setGeometry(10, 50, 91, 17)

        self.rdbutton5 = QRadioButton("infinite", self.frame2)
        self.rdbutton5.setObjectName("infinite")
        self.rdbutton5.setChecked(True)
        self.rdbutton5.setGeometry(10, 90, 91, 17)

        self.buttonGroup2 = QButtonGroup(self.frame2)
        self.buttonGroup2.addButton(self.rdbutton4)
        self.buttonGroup2.addButton(self.rdbutton5)

        self.lineEdit2 = QLineEdit(self.frame2)
        self.lineEdit2.setText("100")
        self.lineEdit2.setGeometry(100, 50, 61, 20)

        # ---------

        self.frame3 = QFrame(self)
        self.frame3.setGeometry(20, 180, 191, 121)
        self.frame3.setObjectName("frame3")
        self.frame3.setStyleSheet(u"#frame3 { border: 1px solid black; border-color: black}")

        self.label4 = QLabel("Frequency", self.frame3)
        self.label4.setGeometry(70, 0, 50, 17)

        self.rdbutton6 = QRadioButton("Click per Sec :", self.frame3)
        self.rdbutton6.setObjectName("clickPerSec")
        self.rdbutton6.setChecked(True)
        self.rdbutton6.setGeometry(10, 30, 82, 17)

        self.rdbutton7 = QRadioButton("Delay (ms):", self.frame3)
        self.rdbutton7.setObjectName("Delay")
        self.rdbutton7.setGeometry(10, 60, 82, 17)

        self.buttonGroup3 = QButtonGroup(self.frame3)
        self.buttonGroup3.addButton(self.rdbutton6)
        self.buttonGroup3.addButton(self.rdbutton7)

        self.lineEdit3 = QLineEdit("1", self.frame3)
        self.lineEdit3.setGeometry(100, 30, 71, 20)

        self.lineEdit4 = QLineEdit("1000", self.frame3)
        self.lineEdit4.setGeometry(100, 60, 71, 20)

app = QApplication(sys.argv)
window = MainWindow()

running = False

def on_press(key):
    if key == keyboard.Key.f6:
        print("f6 clicked")
        if running:
            Stop()
        else:
            Start()

def Start():
    global running
    selectedBut = window.buttonGroup2.checkedButton()
    if not running:
        running = True
        if selectedBut.objectName() == "infinite":
            threading.Thread(target=click_infinite, daemon=True).start()
        elif selectedBut.objectName() == "repeat":
            threading.Thread(target=click_step, daemon=True).start()

def click_infinite():
    global running
    selectedBut = window.buttonGroup.checkedButton()
    selectedTime = choose_time_type()
    while running:
        mouse.click(selectedBut.objectName())
        time.sleep(float(selectedTime))

def click_step():
    global running
    flag = 0
    selectedBut = window.buttonGroup.checkedButton()
    selectedTime = choose_time_type()
    destination_flag = int(window.lineEdit2.text())
    while running:
        mouse.click(selectedBut.objectName())
        flag += 1
        time.sleep(float(selectedTime))
        if flag == destination_flag:
            print("Reached to step size")
            Stop()

def choose_time_type():
    if window.buttonGroup3.checkedButton().objectName() == "clickPerSec":
        selectedTime = 1 / int(window.lineEdit3.text())
    else:
        selectedTime = int(window.lineEdit4.text()) / 1000
    return selectedTime

def Stop():
    global running
    running = False
    print("Stopped!")

window.button.clicked.connect(Start)
window.button2.clicked.connect(Stop)

listener = keyboard.Listener(on_press=on_press)
listener.start()


window.show()
sys.exit(app.exec_())
