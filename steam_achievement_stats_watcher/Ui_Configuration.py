import sys
from PyQt5.QtWidgets import QDialog
import ui

class Ui_Configuration(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Configuration()
        self.ui.setupUi(self)
        #self.ui.Action.clicked.connect(self.configButtonBox)
        self.show()
    def message(self):
        #self.ui.Print.setText("Hello " + self.ui.Input1.text() + ", your age is " + self.ui.Input2.text())
        pass