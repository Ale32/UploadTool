__author__ = 'a.paoletti'

from core import sql


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


def check_texture_type():
    pass
