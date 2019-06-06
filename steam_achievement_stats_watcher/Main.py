import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, qApp
import steam_achievement_stats_watcher
import ui


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Main()
        self.ui.setupUi(self)
        # Enable menu buttons
        self.ui.AddGame.triggered.connect(qApp.quit)
        self.ui.Configure.triggered.connect(self.config_window)
        self.show()

    def config_window(self):
        print("config_window")
        widget = QDialog(self)
        ui = ui.Ui_Configuration()
        ui.setupUi(widget)
        widget.exec_()
        widget.show()
