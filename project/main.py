import sys
import socket
import threading

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow


class StartedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("windows/started_window.ui", self)
        self.pushButton_play.clicked.connect(self.go_to_enter_number_window)
        self.setStyleSheet("#Started_Window{border-image:url(static/cow.jpg)}")
        self.setFixedSize(640, 780)
        self.enter_number_window = EnterNumberWindow()

    def go_to_enter_number_window(self):
        self.close()
        self.enter_number_window.show()


class AbstractWindow(QMainWindow):
    def __init__(self):
        super(AbstractWindow, self).__init__()

    def on_click(self, number, button):
        text = self.label_4.text() + f'{number}'
        self.label_4.setText(f"{text}")
        button.setEnabled(False)
        self.check()

    def on_click_0(self):
        self.on_click('0', self.pushButton_0)

    def on_click_delete(self):
        if len(self.label_4.text()) != 0:
            self.in_label(True)
        self.label_4.setText('')
        self.pushButton_enter.setEnabled(False)

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


    def in_label(self, booll):
        buttons = [self.pushButton_0, self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4,
                        self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9]
        for btn in buttons:
            btn.setEnabled(booll)

    def check(self):
        if len(self.label_4.text()) == 4:
            self.in_label(False)
            self.pushButton_enter.setEnabled(True)


class EnterNumberWindow(AbstractWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("windows/enter_number_window.ui", self)
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
        self.pushButton_enter.clicked.connect(self.go_to_main_window)

    def go_to_main_window(self):
        self.enter_number_window = MainWindow(self.label_4.text())
        self.close()
        self.enter_number_window.show()


class MainWindow(AbstractWindow):
    def __init__(self, number):
        super().__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 6080))
        self.number = str(number)
        uic.loadUi("windows/main.ui", self)
        self.setStyleSheet("#MainWindow{border-image:url(static/background.jpg)}")
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
        self.pushButton_enter.clicked.connect(self.write)
        self.pushButton_game_again.clicked.connect(self.game_again)
        self.pushButton_game_again_2.clicked.connect(self.game_again)
        self.pushButton_game_again_3.clicked.connect(self.game_again)
        self.client.send(self.number.encode('ascii'))
        self.widget_3.hide()
        self.widget_4.hide()
        self.widget_5.hide()
        self.prewinner = 0
        self.send_prewinner = 0
        path = 'static/loading.gif'
        gif = QtGui.QMovie(path)  # !!!
        self.label_loading.setMovie(gif)
        gif.start()
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def receive(self):
        self.widget_2.hide()
        first_player = 1
        while True:
            try:
                # пытаемся получить сообщение
                message = self.client.recv(1024).decode('ascii')
                if message == "nostartgame":
                    self.widget.hide()
                    self.widget_2.show()
                elif message == "startgame":
                    self.widget_2.hide()
                    self.widget.show()
                    self.in_label(False)
                    first_player = 2
                elif message != "NUMBER":
                    if message == 'prewinner':
                        self.prewinner = 1
                    elif first_player == 1:
                        self.write_number(message + ',1')
                    else:
                        self.write_number(message + ',2')

            except:
                # в случае любой ошибки лочим открытые инпуты и выводим ошибку
                self.My_fied.setText("Error! Reload app")
                self.My_fied.setEnabled(False)
                # закрываем клиент
                self.client.close()
                break

    def write(self):
        message = self.label_4.text()
        self.client.send(message.encode('ascii'))



    def write_number(self, message):
        message = message.split(',')
        input_number = message[0]
        hidden_number = message[1]
        player = int(message[2])
        number = str(self.label_4.text())
        cows = 0
        bulls = 0
        j = 0
        for i in input_number:
            if hidden_number[j] == i:
                bulls += 1
            elif i in hidden_number:
                cows += 1
            j += 1
        res = f'{input_number}' + ' ' * 14 + f'{bulls}' + ' ' * 14 + f'{cows}'
        self.on_click_delete()

        if number == input_number:
            self.My_fied.append(res)
            self.in_label(False)
            if bulls == 4 and player == 1:
                self.send_prewinner = 1
                self.client.send('prewinner'.encode('ascii'))
            elif bulls != 4 and player == 2 and self.prewinner == 1:
                self.setStyleSheet("#MainWindow{border-image:url(static/lose.jpg)}")
                self.loser()
            elif bulls == 4 and player == 2:
                if self.prewinner == 1:
                    self.draw()
                else:
                    self.winner()
        else:
            self.Opponent_fied.append(res)
            self.in_label(True)
            if bulls != 4 and player == 1 and self.send_prewinner == 1:
                self.winner()
            elif bulls == 4 and player == 1:
                self.in_label(False)
                if self.send_prewinner == 1:
                    self.draw()
                else:
                    self.setStyleSheet("#MainWindow{border-image:url(static/lose.jpg)}")
                    self.loser()

    def winner(self):
        self.end_game()
        self.widget.hide()
        self.setStyleSheet("#MainWindow{border-image:url(static/win.jpg)}")
        self.widget_3.show()

    def loser(self):
        self.end_game()
        self.widget.hide()
        self.widget_4.show()

    def draw(self):
        self.end_game()
        self.setStyleSheet("#MainWindow{border-image:url(static/draw.jpg)}")
        self.widget.hide()
        self.widget_5.show()

    def game_again(self):
        self.close()
        self.backwindow = EnterNumberWindow()
        self.backwindow.show()

    def end_game(self):
        self.client.send('endgame'.encode('ascii'))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = StartedWindow()
    first.show()
    sys.exit(app.exec())
