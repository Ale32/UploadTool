__author__ = 'a.paoletti'

from PySide import QtGui
import sys
import os

import ui.MainWindow as MainWindow


if __name__ == "__main__":
    sys.path.append(os.path.dirname(__file__))

    app = QtGui.QApplication(sys.argv)

    window = MainWindow.UploadToolUI()
    window.show()

    sys.exit(app.exec_())
