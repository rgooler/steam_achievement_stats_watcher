import steam_achievement_stats_watcher
from PyQt5.QtWidgets import QApplication
import sys

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = steam_achievement_stats_watcher.Ui_Configuration()
    w.show()
    sys.exit(app.exec_())
