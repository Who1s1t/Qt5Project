import sqlite3
import sys
import datetime
import requests
from PyQt5.QtWidgets import QApplication, QWidget
from ui_file import Ui_App


class App(QWidget, Ui_App):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("convert.db")
        self.cur = self.con.cursor()
        self.start()
        self.create_db()
        self.set()
        self.check_connection()

    def create_db(self):  # Создаём таблицу при её отсутствие и обновляем её
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS course (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        iso_code VARCHAR (5),
                        value_ DECIMAL (10, 6),
                        update_ DATETIME
                    )""")
        self.con.commit()
        if self.check_connection():
            self.update_db()

    def check_connection(self):  # Проверяем подключение к интернету
        try:
            requests.get('https://www.google.ru')
            return 1
        except Exception:
            self.bupdate.setText("Нет интернет подключения \n Повторить попытку")
            return 0

    def start(self):
        self.setupUi(self)
        self.show()

    def set(self):
        data1 = self.cur.execute("""SELECT iso_code FROM course""").fetchall()
        data = [i[0] for i in data1]
        self.b.addItems(data)
        self.b_2.addItems(data)
        self.iz.setText("сколько")
        self.v.setText("получите")
        self.but.setText("Конвертировать")
        self.bupdate.setText("Обновить Базу Данных")
        self.but.clicked.connect(lambda: self.display())
        self.bupdate.clicked.connect(lambda: self.update_db())

    def display(self):  # Вывод результата
        try:
            res = self.convert(float(self.iz.text()), str(self.b.currentText()), str(self.b_2.currentText()))
            self.v.setText(str(res))
        except ValueError:
            self.iz.setText(str("Неверное число"))

    def update_db(self):  # Обновляем значения в таблице
        if self.check_connection():
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
            self.bupdate.setText("Обновить Базу Данных")

    def convert(self, value, from_, to):  # Конвертируем валюту
        data_from = self.cur.execute(f"""SELECT value_ FROM course WHERE iso_code = '{from_}'""").fetchall()
        data_from = data_from[0][0]
        data_to = self.cur.execute(f"""SELECT value_ FROM course WHERE iso_code = '{to}'""").fetchall()
        data_to = data_to[0][0]
        from_USD = value / data_from
        res = data_to * from_USD
        return res


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.excepthook = except_hook
    sys.exit(app.exec())
