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


def version(asset_dir):
    """ Search into asset_path folders call vXXX

    Return string of the version in the form vXXX incrementing the last one founded
    """
    regex = ur"^v([\d]{3})$"
    new_version = 'v001'
    versions = []

    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)

    # look for dirs into asset dir searching for vXXX
    subdirs = [name for name in os.listdir(asset_dir) if os.path.isdir(os.path.join(asset_dir, name))]

    for d in subdirs:
        print d
        matches = re.finditer(regex, d)

        for match_num, match in enumerate(matches):
            if match.groups()[0]:
                versions.append(match.groups()[0])

        latest_version = sorted(versions)[-1]
        new_version = 'v' + str(int(latest_version) + 1).zfill(3)

    return new_version


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
