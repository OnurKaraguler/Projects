import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout, \
    QLabel, QVBoxLayout, QPushButton, QComboBox, QGroupBox, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import requests, threading, time
from bs4 import BeautifulSoup as BS

class ExchangeCurrency(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exchange Currency')
        self.setGeometry(400,200,380,400)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layout()
        self.timer = threading.Timer(2.0, self.currentCurrency)
        self.timer.start()

    def widgets(self):
        self.currencyBought_co = QComboBox()
        self.currencyBought_co.addItems(['USD','EUR','TRY'])
        self.currencyReceived_co = QComboBox()
        self.currencyReceived_co.addItems(['USD','EUR','TRY'])

        self.amount_le = QLineEdit('1')

        self.currentCurrency_lb = QLabel()
        self.currentCurrency_lb.setStyleSheet("color: blue;""background-color: pink;""font:12pt Times Bold;"
                        "selection-color: yellow;""border:2px solid gray;""border-radius:15px;"
                        "padding: 10px;""selection-background-color: blue;")
        self.updating_lb = QLabel()
        self.updating_lb.setStyleSheet("color: blue;""background-color: yellow;""font:12pt Times Bold;"
                        "selection-color: yellow;""border:2px solid gray;""border-radius:15px;"
                        "padding: 10px;""selection-background-color: blue;")
        self.result_lb = QLabel()
        self.result_lb.setStyleSheet("color: blue;""background-color: yellow;""font:12pt Times Bold;"
                        "selection-color: yellow;""border:2px solid gray;""border-radius:15px;"
                        "padding: 10px;""selection-background-color: blue;")
        self.result_lb.setAlignment(Qt.AlignTop)

        self.calc_btn = QPushButton('Exchange')
        # self.calc_btn.setStyleSheet("background-color: #9bc9ff;""border-style: outset;""border-width: 2px;"
        #                             "border-radius: 10px;""border-color: beige;""font: bold 14px;"
        #                             "min-width: 10em;""padding: 6px;")
        self.calc_btn.clicked.connect(self.exchangeCalculation)

        self.closeUpd_btn = QPushButton('Stop Update')
        self.closeUpd_btn.setStyleSheet("background-color: red;""border-style: outset;""border-width: 2px;"
                                    "border-radius: 10px;""border-color: beige;""font: bold 14px;"
                                    "min-width: 10em;""padding: 6px;")
        self.closeUpd_btn.clicked.connect(self.closeUpdate)

        self.openUpd_btn = QPushButton('Update')
        self.openUpd_btn.setStyleSheet("background-color: green;""border-style: outset;""border-width: 2px;"
                                    "border-radius: 10px;""border-color: beige;""font: bold 14px;"
                                    "min-width: 10em;""padding: 6px;")
        self.openUpd_btn.clicked.connect(self.currentCurrency)

    def layout(self):
        self.mainTopLayout = QFormLayout()
        self.mainMiddleLayout = QHBoxLayout()
        self.mainBottomLayout = QHBoxLayout()
        self.mainLayout = QVBoxLayout()

        self.topGroupBox = QGroupBox('Currency Exchange')
        self.topGroupBox.setStyleSheet(""" QGroupBox{background-color: #9bc9ff; font:12pt Times Bold; color:white;
        border:2px solid gray; border-radius:15px;}""")
        # self.topGroupBox.setAlignment(Qt.AlignBottom)
        # self.topGroupBox.setFixedSize(350,100)
        # self.topGroupBox.setCheckable(True)
        # self.topGroupBox.setAlignment(1)

        self.topGroupBox.setLayout(self.mainTopLayout)

        self.mainLayout.addWidget(self.topGroupBox,25)
        self.mainLayout.addLayout(self.mainMiddleLayout)
        self.mainLayout.addLayout(self.mainBottomLayout)
        self.setLayout(self.mainLayout)
        ##################Add Widgets##############
        self.mainTopLayout.addRow('Currency to sell',self.currencyBought_co)
        self.mainTopLayout.addRow('Currency to recieve',self.currencyReceived_co)
        self.mainTopLayout.addRow('Amount',self.amount_le)
        self.mainTopLayout.addRow('',self.calc_btn)

        # self.mainTopLayout.addStretch()
        # self.mainTopLayout.addWidget(self.calc_btn)

        self.mainBottomLayout.addWidget(self.closeUpd_btn)
        self.mainBottomLayout.addWidget(self.openUpd_btn)

        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addWidget(self.currentCurrency_lb,20)
        self.mainLayout.addWidget(self.updating_lb,10)
        self.mainLayout.addWidget(self.result_lb,10)

    def currentCurrency(self):
        start = time.time()
        self.currencySold = self.currencyBought_co.currentText()
        self.currencyReceived = self.currencyReceived_co.currentText()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        }
        with requests.Session() as ses:
            url_usd_try = 'https://tr.investing.com/currencies/usd-try'
            url_eur_try = 'https://tr.investing.com/currencies/eur-try'
            url_eur_usd = 'https://tr.investing.com/currencies/eur-usd'

            r_usd_try = ses.get(url_usd_try, headers=headers)
            r_eur_try = ses.get(url_eur_try, headers=headers)
            r_eur_usd = ses.get(url_eur_usd, headers=headers)

            soup_usd_try = BS(r_usd_try.content, 'html.parser')
            soup_eur_try = BS(r_eur_try.content, 'html.parser')
            soup_eur_usd = BS(r_eur_usd.content, 'html.parser')

            list_usd_try = soup_usd_try.find_all('div', {"class": "overViewBox instrument"})
            list_eur_try = soup_eur_try.find_all('div', {"class": "overViewBox instrument"})
            list_eur_usd = soup_eur_usd.find_all('div', {"class": "overViewBox instrument"})

            for usd_try in list_usd_try:
                self.dollar_try = usd_try.find("div", {"class": "top bold inlineblock"}).find("span").text
                self.dollar_try = float((self.dollar_try).replace(',', '.'))

            for eur_try in list_eur_try:
                self.euro_try = eur_try.find("div", {"class": "top bold inlineblock"}).find("span").text
                self.euro_try = float((self.euro_try).replace(',', '.'))

            for eur_usd in list_eur_usd:
                self.euro_usd = eur_usd.find("div", {"class": "top bold inlineblock"}).find("span").text
                self.euro_usd = float((self.euro_usd).replace(',','.'))

            self.currentCurrency_lb.setText(f"USD = {self.dollar_try} TRY"
                                            f"\nEUR = {self.euro_try} TRY"
                                            f"\nEUR = {self.euro_usd} USD")

        self.amount = self.amount_le.text()
        try:
            amount = int(self.amount)
            if (self.currencySold == 'USD' and self.currencyReceived == 'TRY'):
                result = amount * self.dollar_try
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'TRY' and self.currencyReceived == 'USD'):
                result = amount / self.dollar_try
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'EUR' and self.currencyReceived == 'TRY'):
                result = amount * self.euro_try
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'TRY' and self.currencyReceived == 'EUR'):
                result = amount / self.euro_try
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'EUR' and self.currencyReceived == 'USD'):
                result = amount * self.euro_usd
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'USD' and self.currencyReceived == 'EUR'):
                result = amount / self.euro_usd
                self.result_lb.setText(f'{result}')
        except Exception:
            QMessageBox.information(self, 'Info', 'Input can only be a number')

        end =time.time()
        print(f'time taken: {end - start}')
        self.updating_lb.setText('Updating is running.')
        self.timer = threading.Timer(5.0, self.currentCurrency)
        self.timer.start()

    def closeUpdate(self):
        self.timer.cancel()
        self.updating_lb.setText('Updating is stopped.')

    def exchangeCalculation(self):
        self.currencyBought = self.currencyBought_co.currentText()
        self.currencyReceived = self.currencyReceived_co.currentText()
        self.amount = self.amount_le.text()

        try:
            amount = int(self.amount)
            if (self.currencySold == 'USD' and self.currencyReceived == 'TRY'):
                result = amount * self.dollar_try
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'TRY' and self.currencyReceived == 'USD'):
                result = amount / self.dollar_try
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'EUR' and self.currencyReceived == 'TRY'):
                result = amount * self.euro_try
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'TRY' and self.currencyReceived == 'EUR'):
                result = amount / self.euro_try
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'EUR' and self.currencyReceived == 'USD'):
                result = amount * self.euro_usd
                self.result_lb.setText(f'{result}')
            elif (self.currencySold == 'USD' and self.currencyReceived == 'EUR'):
                result = amount / self.euro_usd
                self.result_lb.setText(f'{result}')
        except Exception:
            QMessageBox.information(self, 'Info', 'Input can only be a number')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExchangeCurrency()
    sys.exit(app.exec_())