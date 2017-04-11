__author__ = 'a.paoletti'

from core import sql
from core import debug
import os
import re

from config import ConfigReader


def get_projects():
    """
    Return a list of (id, name) of projects
    """
    data = sql.list_projects()
    names = [(d['id'], d['name']) for d in data]
    return names


def get_groups(id_project):
    """
    Return a list of (id, name) of groups
    """
    data = sql.list_groups(id_project)
    names = [(d['id'], d['name']) for d in data]
    return names


def get_assets(id_group):
    """
    Return a list of (id, name) of assets
    """
    data = sql.list_assets(id_group)
    names = [(d['id'], d['name']) for d in data]
    return names


def file_type(filename):
    ext = os.path.splitext(filename)[1].replace('.', '')

    return ConfigReader.file_type_from_ext(ext)


def asset_versioning(asset_id):
    data = sql.asset_versioning(asset_id)

    return data[0]['versioning']


def version(asset_dir, new_version):
    """ Search into asset_path folders call vXXX
    If new_version is True, return string of the version in the form vXXX incrementing the last one founded
    If is False, return the current version if exist
    """
    regex = ur"^v([\d]{3})$"
    version_found = False
    versions = []

    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)

    # look for dirs into asset dir searching for vXXX
    subdirs = [name for name in os.listdir(asset_dir) if os.path.isdir(os.path.join(asset_dir, name))]

    for d in subdirs:
        matches = re.finditer(regex, d)

        for match_num, match in enumerate(matches):
            if match.groups()[0]:
                version_found = True
                versions.append(match.groups()[0])

    if version_found is True:
        latest_version = sorted(versions)[-1]
        
        if new_version is False:
            return 'v' + latest_version.zfill(3)

        return 'v' + str(int(latest_version) + 1).zfill(3)

    else:
        return 'v001'


def generate_name(filename, asset_name):

    ext = os.path.splitext(filename)[1].replace('.', '')

    f_type = file_type(filename)

    if f_type is None:
        debug.show_error("CANNOT RECOGNIZE FILE TYPE. EXTENSION UNKNOWN.")
        return

    prefix = ConfigReader.asset_prefix(f_type)

    suffix = ''
    if f_type == 'textures':
        suffix = ConfigReader.texture_suffix(filename)

        if not suffix:
            debug.show_error("Can't recognize texture type from the name. Check texture naming rules!")
            return

    # complete name
    name = prefix + '_' + asset_name

    if suffix:
        name += '_' + suffix

    name += '.' + ext
    return name


def instructions():
    """ Format a text with app istructions

    Dynamically created from config data.
    This is useful to display informations on GUI.

    :return: An HTML text representing instructions
    """
    txt_naming = ConfigReader.texture_naming_dict()

    text = "<b>Texture naming rules:</b><br>(put an underscore _ at the end of file name)"

    for key, value in txt_naming.iteritems():
        text += "<br>- {0}: {1}".format(key, ', '.join(a for a in value['text']))

    text += "<br>"
    text += "<br><b>File formats:</b>"
    text += "<br>Meshes:"
    text += ConfigReader.generate_file_filter()
    text += "<br>Textures:"
    text += ConfigReader.generate_texture_filter()

    return text
