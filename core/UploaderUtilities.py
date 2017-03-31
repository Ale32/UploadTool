__author__ = 'a.paoletti'

from core import sql
import os

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


def generate_name(filename, asset_name):

    ext = os.path.splitext(filename)[1].replace('.', '')

    f_type = file_type(filename)

    prefix = ConfigReader.asset_prefix(f_type)

    suffix = ''
    if f_type == 'textures':
        suffix = ConfigReader.texture_suffix(filename)

        if not suffix:
            raise Exception("Can't recognize texture type from the name.")

    # complete name
    name = prefix + '_' + asset_name

    if suffix:
        name += '_' + suffix

    name += '.' + ext
    return name
