__author__ = 'a.paoletti'

from PySide import QtCore, QtGui, QtUiTools
import sys


class UploadToolUI(object):

    def __init__(self):
        self.ui = self.load_ui_widget("MainWindow.ui")
        self.setup_connections()

    def setup_connections(self):
        self.ui.button_fbx.clicked.connect(self.get_files)

    def get_files(self):
        f_dialog = QtGui.QFileDialog()
        f_dialog.setFileMode(QtGui.QFileDialog.ExistingFiles)
        f_dialog.setDirectory("C:\\Users\\a.paoletti\\Desktop\\STUFF")
        f_dialog.setNameFilter("Assets data (*.fbx *.png *.jpg *.tga)")
        f_dialog.selectNameFilter("*.fbx *.png *.jpg *.tga")

        if f_dialog.exec_():
            filenames = f_dialog.selectedFiles()
            self.ui.listWidget.addItems(filenames)

    @staticmethod
    def load_ui_widget(uifilename, parent=None):
        loader = QtUiTools.QUiLoader()

        uifile = QtCore.QFile(uifilename)
        uifile.open(QtCore.QFile.ReadOnly)

        ui = loader.load(uifile, parent)
        uifile.close()

        return ui

    def show(self):
        self.ui.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    window = UploadToolUI()
    window.show()

    sys.exit(app.exec_())
