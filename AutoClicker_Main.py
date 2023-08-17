from AutoClicker_frontend import MainWindow
from PyQt5.QtWidgets import *
import sys
import threading
import time
import mouse
from pynput import keyboard

app = QApplication(sys.argv)
window = MainWindow()

boolean=False

def on_press(key):
    if key==keyboard.Key.f6:
        boolean = not boolean

def baslat():
    global boolean
    selectedBut=window.buttonGroup2.checkedButton()
    if boolean is False:
        boolean=True
        if selectedBut.objectName() == "sonsuz":
            threading.Thread(target=clickInfinite,daemon=True).start()
        elif selectedBut.objectName() =="tekrar":
            threading.Thread(target=clickStep,daemon=True).start()

def clickInfinite():
    global boolean
    selectedBut=window.buttonGroup.checkedButton()
    selectedTime=chooseTimeType()
    flag=0
    while boolean is True:
        mouse.click(selectedBut.objectName())
        time.sleep(float(selectedTime))

def clickStep():
    global boolean
    flag=0
    selectedBut=window.buttonGroup.checkedButton()
    selectedTime=chooseTimeType()
    destination_flag=int(window.lineEdit2.text())
    while boolean is True:
        mouse.click(selectedBut.objectName())
        flag+=1
        time.sleep(float(selectedTime))
        if flag==destination_flag:
            print("adım sayısına ulaşıldı")
            print(selectedTime)
            durdur()

def chooseTimeType():
    if window.buttonGroup3.checkedButton().objectName() == "snBasi":
        selectedTime=1/int(window.lineEdit3.text())
    else:
        selectedTime=int(window.lineEdit4.text())/1000
    print(selectedTime)
    return selectedTime

def durdur():
    global boolean
    boolean=False
    print("durduruldu!")

window.button.clicked.connect(baslat)
window.button2.clicked.connect(durdur)

listener=keyboard.Listener(on_press=on_press)
listener.start()

window.show()
app.exec()