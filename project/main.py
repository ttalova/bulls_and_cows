import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class Started_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("started_window.ui", self)
        self.pushButton_play.clicked.connect(self.go_to_enter_number_window)
        self.setStyleSheet("#Started_Window{border-image:url(static/cow.jpg)}")
        self.setFixedSize(640, 780)
    def go_to_enter_number_window(self):
        self.enter_number_window = Enter_Number_Window()
        self.close()
        self.enter_number_window.show()

    # Form_started_window, Window_started_window = uic.loadUiType("started_window.ui")
    # app = QApplication([])
    # window_started_window = Window_started_window()
    # window_started_window.setStyleSheet("#Started_Window{border-image:url(static/cow.jpg)}")
    # window_started_window.setFixedSize(640, 780)
    # form_started_window = Form_started_window()
    # form_started_window.setupUi(window_started_window)
    # window_started_window.show()
    # form_started_window.pushButton_play.clicked.connect(Enter_Number_Window)
    # form_started_window.pushButton_play.clicked.connect(window_started_window.close)
    # app.exec_()



class Enter_Number_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("enter_number_window.ui", self)
        self.setStyleSheet("#EnterNumberWindow{border-image:url(static/background.jpg)}")
        self.setFixedSize(640, 780)
        self.pushButton_enter.setEnabled(False)
        self.pushButton_0.clicked.connect(self.on_click_0)
        self.pushButton_1.clicked.connect(self.on_click_1)
        self.pushButton_2.clicked.connect(self.on_click_2)
        self.pushButton_3.clicked.connect(self.on_click_3)
        self.pushButton_4.clicked.connect(self.on_click_4)
        self.pushButton_5.clicked.connect(self.on_click_5)
        self.pushButton_6.clicked.connect(self.on_click_6)
        self.pushButton_7.clicked.connect(self.on_click_7)
        self.pushButton_8.clicked.connect(self.on_click_8)
        self.pushButton_9.clicked.connect(self.on_click_9)
        self.pushButton_delete.clicked.connect(self.on_click_delete)

    def on_click(self, number, button):
        text = self.label_4.text() + f'{number}'
        self.label_4.setText(f"{text}")
        button.setEnabled(False)
        self.check()

    def on_click_0(self):
        self.on_click('0', self.pushButton_0)

    def on_click_1(self):
        self.on_click('1', self.pushButton_1)

    def on_click_2(self):
        self.on_click('2', self.pushButton_2)

    def on_click_3(self):
        self.on_click('3', self.pushButton_3)

    def on_click_4(self):
        self.on_click('4', self.pushButton_4)

    def on_click_5(self):
        self.on_click('5', self.pushButton_5)

    def on_click_6(self):
        self.on_click('6', self.pushButton_6)

    def on_click_7(self):
        self.on_click('7', self.pushButton_7)

    def on_click_8(self):
        self.on_click('8', self.pushButton_8)

    def on_click_9(self):
        self.on_click('9', self.pushButton_9)

    def on_click_delete(self):
        self.label_4.setText('')
        self.in_label(True)
        self.pushButton_enter.setEnabled(False)


    def in_label(self, booll):
        self.pushButton_0.setEnabled(booll)
        self.pushButton_1.setEnabled(booll)
        self.pushButton_2.setEnabled(booll)
        self.pushButton_3.setEnabled(booll)
        self.pushButton_4.setEnabled(booll)
        self.pushButton_5.setEnabled(booll)
        self.pushButton_6.setEnabled(booll)
        self.pushButton_7.setEnabled(booll)
        self.pushButton_8.setEnabled(booll)
        self.pushButton_9.setEnabled(booll)


    def check(self):
        if len(self.label_4.text()) == 4:
            self.in_label(False)
            self.pushButton_enter.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = Started_Window()
    first.show()
    sys.exit(app.exec_())


