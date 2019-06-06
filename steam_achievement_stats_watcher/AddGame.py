import sys
from PyQt5.QtWidgets import QDialog
import ui


class AddGame(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_AddGame()
        self.ui.setupUi(self)
        self.show()
