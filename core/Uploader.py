"""
UPLOADER CLASS
"""
import os
import shutil
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

    def directory(self):
        return self.dir

    def upload(self, file_path):
        # generate asset name from file basename
        asset_name = UploaderUtilities.generate_name(os.path.basename(file_path), self.asset)

        if not asset_name:
            return

        # set the output path
        file_output = os.path.join(self.dir, asset_name)

        try:
            # shutil.copy2(src, dst)
            print 'SOURCE ', file_path
            print 'DEST ', file_output

        except shutil.Error as e:
            print('Error copying file: %s' % e)

        except IOError as e:
            print('Error copying file: %s' % e)
