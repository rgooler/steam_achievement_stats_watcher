import sys
from PyQt5.QtWidgets import QDialog, QApplication
import ui

class MyAPP(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Configuration()
        self.ui.setupUi(self)
        #self.ui.Action.clicked.connect(self.message)
        self.show()
    def message(self):
        #self.ui.Print.setText("Hello " + self.ui.Input1.text() + ", your age is " + self.ui.Input2.text())
        pass

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyAPP()
    w.show()
    sys.exit(app.exec_())
