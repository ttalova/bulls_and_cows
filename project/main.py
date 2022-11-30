from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

from helpfull_functions import *

def Started_Window():
    Form_started_window, Window_started_window = uic.loadUiType("started_window.ui")
    app = QApplication([])
    window_started_window = Window_started_window()
    window_started_window.setStyleSheet("#Started_Window{border-image:url(static/cow.jpg)}")
    window_started_window.setFixedSize(640, 780)
    form_started_window = Form_started_window()
    form_started_window.setupUi(window_started_window)
    window_started_window.show()
    form_started_window.pushButton_play.clicked.connect(Enter_Number_Window)
    form_started_window.pushButton_play.clicked.connect(window_started_window.close)
    app.exec_()



def Enter_Number_Window():
    global window, form
    Form, Window = uic.loadUiType("enter_number_window.ui")
    window = Window()
    window.setStyleSheet("#EnterNumberWindow{border-image:url(static/background.jpg)}")
    window.setFixedSize(640, 780)
    form = Form()
    form.setupUi(window)
    window.show()
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

if __name__ == '__main__':
    Started_Window()


