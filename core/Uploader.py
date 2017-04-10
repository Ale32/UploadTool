"""
UPLOADER CLASS
"""
import os
import shutil

from config import ConfigReader
from core import UploaderUtilities
from core import tracker


class Uploader(object):
    """ Class that handles the upload of file on project content

    It requires a list of (id, name) for project, group, asset
    """

    def __init__(self, project, group, asset):
        # project data
        self.project_id = project[0]
        self.project_name = project[1]

        # group data
        self.group_id = group[0]
        self.group_name = group[1]

        # asset data
        self.asset_id = asset[0]
        self.asset_name = asset[1]

        self.dir = ''
        self.generate_dir_path()

        # add version folder if asset require it
        if UploaderUtilities.asset_versioning(self.asset_id) in ['true', 'True', '1']:
            self.add_versioning_folder()

    def generate_dir_path(self):
        self.dir = os.path.join(
            '//',
            ConfigReader.server_name(),
            ConfigReader.share_name(),
            ConfigReader.content_name(),
            self.project_name,
            'assets',
            self.group_name,
            self.asset_name
        )
        os.path.normcase(self.dir)

    def add_versioning_folder(self):
        self.dir = os.path.join(
            self.dir,
            UploaderUtilities.version(self.dir)
        )

    def directory(self):
        return self.dir

    def log(self):
        tracker.track_it(self.dir)

    def upload(self, file_path):
        # generate asset name from file basename
        asset_name = UploaderUtilities.generate_name(os.path.basename(file_path), self.asset_name)

        if not asset_name:
            return

        # set the output path
        file_output = os.path.join(self.dir, asset_name).replace("\\", "/")
        output_dir = os.path.dirname(file_output)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            # print 'SOURCE ', file_path
            # print 'DEST ', file_output
            shutil.copy2(file_path, file_output)

        except shutil.Error as e:
            print('Error copying file: %s' % e)

        except IOError as e:
            print('Error copying file: %s' % e)
