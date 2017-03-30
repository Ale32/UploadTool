__author__ = 'a.paoletti'

from PySide import QtGui
import sys

import ui.MainWindow as MainWindow


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    window = MainWindow.UploadToolUI()
    window.show()

    sys.exit(app.exec_())
