import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from GenerateMsg import generateMsg
from SendMsg import sendMsg
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app.ui", self)
        self.dateTimeInput.setCalendarPopup(True)
        self.createMsgButton.clicked.connect(self.createMsg)
        self.retryButton.clicked.connect(self.createMsg)
        self.msg = ""

    def test(self):
        print("LISTENER!!!!")

    def findSleepSeconds(self, date):
        return 0

    def createMsg(self):
        prompt = self.promptInput.toPlainText()
        msg = generateMsg(prompt)
        self.msg = msg
        self.msgInputDisplay.setPlainText(msg)

    def sendMsg(self):
        phoneNumber = self.phoneInput.toPlainText()
        date = self.dateTimeInput.date()
        msgTime = self.dateTimeInput.time()
        sleepTime = self.findSleepSeconds(date)
        time.sleep(sleepTime)
        if self.msg:
            sendMsg(phoneNumber, msgTime.hour(), msgTime.minute() + 2, self.msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())
