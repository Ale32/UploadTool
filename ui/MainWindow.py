__author__ = 'a.paoletti'

from PySide import QtCore, QtGui, QtUiTools

from core import UploaderUtilities


class UploadToolUI(object):

    def __init__(self):
        self.ui = self.load_ui_widget("ui/MainWindow.ui")

        self.setup_connections()

        self.fill_projects()

    def setup_connections(self):
        self.ui.button_fbx.clicked.connect(self.get_files)

        # connect projects
        self.ui.comboBox_projects.currentIndexChanged[int].connect(self.fill_groups)

        # connect groups
        self.ui.comboBox_group.currentIndexChanged[int].connect(self.fill_assets)

        # self.ui.button_upload.clicked.connect(self.test)

    def test(self):
        print self.ui.comboBox_projects.itemData(self.ui.comboBox_projects.currentIndex())

    def fill_projects(self):
        # fill projects combo box
        for project in UploaderUtilities.get_projects():
            id = project[0]
            name = project[1]
            self.ui.comboBox_projects.addItem(name, (id, name))

    def fill_groups(self, index):
        # clear combo box
        self.ui.comboBox_group.clear()

        data = self.ui.comboBox_projects.itemData(index)
        id_project = None
        if data:
            id_project = data[0]

        if id_project:
            # fill group combo box
            for group in UploaderUtilities.get_groups(id_project):
                id = group[0]
                name = group[1]
                self.ui.comboBox_group.addItem(name, (id, name))

    def fill_assets(self, index):
        # clear combo box
        self.ui.comboBox_asset.clear()

        data = self.ui.comboBox_group.itemData(index)
        id_group = None
        if data:
            id_group = data[0]

        if id_group:
            # fill assets combo box
            for asset in UploaderUtilities.get_assets(id_group):
                id = asset[0]
                name = asset[1]
                self.ui.comboBox_asset.addItem(name, (id, name))

    def get_files(self):
        """ Open a file dialog in order to choose files to upload """
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
