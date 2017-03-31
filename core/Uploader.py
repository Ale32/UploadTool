"""
UPLOADER CLASS
"""
import os
from config import ConfigReader
from core import UploaderUtilities


class Uploader(object):
    """ Class that handles the upload of file on project content """

    def __init__(self, project, group, asset):
        self.project = project
        self.group = group
        self.asset = asset

        self.dir = ''
        self.generate_dir_path()

    def generate_dir_path(self):
        self.dir = os.path.join(
            '//',
            ConfigReader.server_name(),
            ConfigReader.share_name(),
            ConfigReader.content_name(),
            self.project,
            self.group,
            self.asset
        )
        os.path.normcase(self.dir)

    def upload(self, file_path):
        filename = os.path.basename(file_path)
        asset_name = UploaderUtilities.generate_name(filename, self.asset)
        print os.path.join(self.dir, asset_name)
