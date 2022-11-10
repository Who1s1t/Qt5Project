import sys
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


def convert(value, from_, to):
    data_from = requests.get(
        f'https://openexchangerates.org/api/latest.json?app_id=2db968ef5bca471f93c0c0e86217a9d5&symbols={from_}').json()
    data_to = requests.get(
        f'https://openexchangerates.org/api/latest.json?app_id=2db968ef5bca471f93c0c0e86217a9d5&symbols={to}').json()
    from_USD = value / data_from["rates"][from_]
    res = data_to["rates"][to] * from_USD
    return res


class App(QWidget):
    def __init__(self):
        self.start()
        self.set()

    def start(self):
        self.ui = uic.loadUi("untitled.ui")
        self.ui.show()

    def set(self):
        data = requests.get(
            'https://openexchangerates.org/api/latest.json?app_id=2db968ef5bca471f93c0c0e86217a9d5').json()
        data = data['rates'].keys()
        self.ui.b.addItems(data)
        self.ui.b_2.addItems(data)
        self.ui.iz.setText("сколько")
        self.ui.v.setText("получите")
        self.ui.but.setText("Конвертировать")
        self.ui.but.clicked.connect(lambda: self.display())

    def display(self):
        res = convert(int(self.ui.iz.text()), str(self.ui.b.currentText()), str(self.ui.b_2.currentText()))
        self.ui.v.setText(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
