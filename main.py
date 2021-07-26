import sys
import yfinance as yf
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ctypes

#  Icon in Windows Taskbar
myAppID = 'stock_worth_today.001'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppID)


class StockWorthToday(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Worth Today")
        self.setWindowIcon(QIcon('icon.png'))

        # Window setup
        self.window = QWidget()
        self.window.setWindowTitle("Stock Worth Today")
        self.window.setMinimumWidth(800)
        self.window.setMinimumHeight(700)
        self.window.setWindowIcon(QIcon('icon.png'))

        # Widget setup

        # Ticker Label
        self.tickerLabel = QLabel("Enter stock ticker symbol:")

        # Ticker Line Edit
        self.tickerLineEdit = QLineEdit()
        self.tickerLineEdit.textChanged.connect(self.auto_capital)  # Auto Capital

        # Initial Investment Label
        self.initialInvestmentLabel = QLabel("Enter initial investment:")

        # Initial Investment Spin Box
        self.initialInvestmentSpinBox = QDoubleSpinBox()
        self.initialInvestmentSpinBox.setMaximum(10000000)
        self.initialInvestmentSpinBox.setMinimum(0.001)
        self.initialInvestmentSpinBox.setValue(1000)
        self.initialInvestmentSpinBox.setPrefix('$')

        # Date Select Label
        self.dateSelectLabel = QLabel("Select Initial Investment Date")

        # Date Select
        self.dateSelect = QCalendarWidget()

        # Run Button
        self.runButton = QPushButton("Run")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tickerLabel)
        self.layout.addWidget(self.tickerLineEdit)
        self.layout.addWidget(self.initialInvestmentLabel)
        self.layout.addWidget(self.initialInvestmentSpinBox)
        self.layout.addWidget(self.dateSelectLabel)
        self.layout.addWidget(self.dateSelect)
        self.layout.addWidget(self.runButton)

        self.window.setLayout(self.layout)

    def auto_capital(self, txt):
        cap_text = txt.title()
        upp_text = txt.upper()  # All Upper Case
        self.tickerLineEdit.setText(upp_text)


def main():
    app = QApplication(sys.argv)
    main_window = StockWorthToday()
    main_window.window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
