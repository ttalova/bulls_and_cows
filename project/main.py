from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
Form, Window = uic.loadUiType("enter_number_window.ui")
app = QApplication([])
window = Window()
window.setStyleSheet("#MainWindow{border-image:url(static/background.jpg)}")
window.setFixedSize(640, 780)
form = Form()
form.setupUi(window)
window.show()


def on_click(number, button):
    text = form.label_4.text() + f'{number}'
    form.label_4.setText(f"{text}")
    button.setEnabled(False)
    check()
def on_click_0():
    on_click('0', form.pushButton_0)

def on_click_1():
    on_click('1', form.pushButton_1)

def on_click_2():
    on_click('2', form.pushButton_2)

def on_click_3():
    on_click('3', form.pushButton_3)

def on_click_4():
    on_click('4', form.pushButton_4)

def on_click_5():
    on_click('5', form.pushButton_5)

def on_click_6():
    on_click('6', form.pushButton_6)

def on_click_7():
    on_click('7', form.pushButton_7)

def on_click_8():
    on_click('8', form.pushButton_8)

def on_click_9():
    on_click('9', form.pushButton_9)

def on_click_delete():
    form.label_4.setText('')
    in_label(True)
    form.pushButton_enter.setEnabled(False)


def in_label(booll):
    form.pushButton_0.setEnabled(booll)
    form.pushButton_1.setEnabled(booll)
    form.pushButton_2.setEnabled(booll)
    form.pushButton_3.setEnabled(booll)
    form.pushButton_4.setEnabled(booll)
    form.pushButton_5.setEnabled(booll)
    form.pushButton_6.setEnabled(booll)
    form.pushButton_7.setEnabled(booll)
    form.pushButton_8.setEnabled(booll)
    form.pushButton_9.setEnabled(booll)


def check():
    if len(form.label_4.text()) == 4:
        in_label(False)
        form.pushButton_enter.setEnabled(True)

form.pushButton_enter.setEnabled(False)
form.pushButton_0.clicked.connect(on_click_0)
form.pushButton_1.clicked.connect(on_click_1)
form.pushButton_2.clicked.connect(on_click_2)
form.pushButton_3.clicked.connect(on_click_3)
form.pushButton_4.clicked.connect(on_click_4)
form.pushButton_5.clicked.connect(on_click_5)
form.pushButton_6.clicked.connect(on_click_6)
form.pushButton_7.clicked.connect(on_click_7)
form.pushButton_8.clicked.connect(on_click_8)
form.pushButton_9.clicked.connect(on_click_9)
form.pushButton_delete.clicked.connect(on_click_delete)


app.exec_()