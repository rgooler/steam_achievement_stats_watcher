import sys
from PyQt5.QtWidgets import QDialog, qApp
import steam_achievement_stats_watcher
import ui


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.main = ui.Ui_Main()
        self.main.setupUi(self)
        # Enable menu buttons
        self.main.AddGameButton.pressed.connect(self.addgame_window)
        self.main.ConfigureButton.pressed.connect(self.config_window)
        self.show()

    def config_window(self):
        widget = QDialog(self)
        dialog = ui.Ui_Configuration()
        dialog.setupUi(widget)
        widget.exec_()
        widget.show()

    def addgame_window(self):
        widget = QDialog(self)
        dialog = ui.Ui_AddGame()
        dialog.setupUi(widget)
        widget.exec_()
        widget.show()
