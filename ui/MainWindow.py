__author__ = 'a.paoletti'

from PySide import QtCore, QtGui, QtUiTools
import os

from core import UploaderUtilities
from core import Uploader
from config import ConfigReader


class UploadToolUI(object):

    def __init__(self):
        self.ui = self.load_ui_widget("ui/MainWindow.ui")

        self.setup_connections()

        self.fill_projects()

        self.populate_convention_table()

    def setup_connections(self):
        self.ui.button_fbx.clicked.connect(self.get_files)

        # clear button
        self.ui.button_clearList.clicked.connect(self.clear_selection)

        # connect projects
        self.ui.comboBox_projects.currentIndexChanged[int].connect(self.fill_groups)

        # connect groups
        self.ui.comboBox_group.currentIndexChanged[int].connect(self.fill_assets)

        self.ui.button_upload.clicked.connect(self.upload)

    def populate_convention_table(self):
        data = ConfigReader.texture_naming_dict()
        self.ui.table_rules.setColumnCount(2)
        self.ui.table_rules.setHorizontalHeaderLabels(['Texture Type', 'Accepted Names'])
        self.ui.table_rules.setRowCount(len(data))

        row = 0
        for key, value in data.iteritems():
            self.ui.table_rules.setItem(row, 0, QtGui.QTableWidgetItem(key))
            self.ui.table_rules.setItem(row, 1, QtGui.QTableWidgetItem(', '.join(value['text'])))
            row += 1

    def upload(self):
        # get data selected
        project = self.ui.comboBox_projects.itemData(self.ui.comboBox_projects.currentIndex())
        group = self.ui.comboBox_group.itemData(self.ui.comboBox_group.currentIndex())
        asset = self.ui.comboBox_asset.itemData(self.ui.comboBox_asset.currentIndex())

        # initialized uploader
        uploader = Uploader.Uploader(project, group, asset)

        # get selected files
        selected_files = []
        for index in xrange(self.ui.listWidget.count()):
            selected_files.append(self.ui.listWidget.item(index).text())

        self.ui.statusbar.showMessage(
            "Copying file into {0}".format(uploader.directory()),
            5000  # milliseconds
        )
        # upload selected files
        for f in selected_files:
            uploader.upload(f)

        # track the upload at the end
        uploader.log()

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
        f_dialog.setDirectory(os.getenv("USERPROFILE"))

        filters = ConfigReader.generate_file_filter() + " " + ConfigReader.generate_texture_filter()
        f_dialog.setNameFilter("Assets data ({})".format(filters))
        f_dialog.selectNameFilter("{}".format(filters))

        if f_dialog.exec_():
            filenames = f_dialog.selectedFiles()
            self.ui.listWidget.addItems(filenames)

    def clear_selection(self):
        self.ui.listWidget.clear()

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
