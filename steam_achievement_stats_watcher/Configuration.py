import sys
from PyQt5.QtWidgets import QDialog
import ui


class Configuration(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Configuration()
        self.ui.setupUi(self)
        self.show()
