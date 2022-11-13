import sqlite3
import sys
import datetime
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class App(QWidget):
    def __init__(self):
        self.con = sqlite3.connect("convert.db")
        self.cur = self.con.cursor()
        self.start()
        self.set()

    def start(self):
        self.ui = uic.loadUi("untitled.ui")
        self.ui.show()

    def set(self):
        data1 = self.cur.execute("""SELECT iso_code FROM course""").fetchall()
        data = [i[0] for i in data1]
        self.ui.b.addItems(data)
        self.ui.b_2.addItems(data)
        self.ui.iz.setText("сколько")
        self.ui.v.setText("получите")
        self.ui.but.setText("Конвертировать")
        self.ui.bupdate.setText("Обновить Базу Данных")
        self.ui.but.clicked.connect(lambda: self.display())
        self.ui.bupdate.clicked.connect(lambda: self.update_db())

    def display(self):
        res = self.convert(float(self.ui.iz.text()), str(self.ui.b.currentText()), str(self.ui.b_2.currentText()))
        self.ui.v.setText(str(res))

    def update_db(self):
        data = requests.get(
            'https://openexchangerates.org/api/latest.json?app_id=2db968ef5bca471f93c0c0e86217a9d5').json()
        data_db = data['rates']
        time = datetime.datetime.now()
        self.cur.execute(f"""DELETE from course""")
        for i in data_db.items():
            iso_code = i[0]
            value = i[1]
            self.cur.execute(
                f"""INSERT INTO course (iso_code,value_,update_) VALUES ('{iso_code}',{value},'{time}')""")
        self.con.commit()

    def convert(self, value, from_, to):
        data_from = self.cur.execute(f"""SELECT value_ FROM course WHERE iso_code = '{from_}'""").fetchall()
        data_from = data_from[0][0]
        data_to = self.cur.execute(f"""SELECT value_ FROM course WHERE iso_code = '{to}'""").fetchall()
        data_to = data_to[0][0]
        from_USD = value / data_from
        res = data_to * from_USD
        return res


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
