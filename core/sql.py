import sqlite3
from config import ConfigReader

connection = None


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect():
    global connection

    if connection is not None:
        return connection

    db_path = ConfigReader.db_path()
    connection = sqlite3.connect(db_path)

    connection.row_factory = dict_factory

    return connection


def list_projects():
    cursor = connect().cursor()
    cursor.execute('SELECT * FROM projects')
    return cursor.fetchall()


def list_groups(project_id=None):
    if project_id is None:
        raise ValueError('No project id specified')

    cursor = connect().cursor()
    cursor.execute('SELECT * FROM groups WHERE id_project = ?', (project_id,))

    return cursor.fetchall()


def list_assets(group_id=None):
    if group_id is None:
        raise ValueError('No group id specified')

    cursor = connect().cursor()
    cursor.execute('SELECT * FROM assets WHERE id_group = ?', (group_id,))

    return cursor.fetchall()


def add_project(project_name=None, project_description=None):
    if project_name is None:
        raise ValueError('Project name must not be None')

    if project_description is None:
        raise ValueError('Project description must not be None')

    cursor = connect().cursor()
    cursor.execute('INSERT INTO projects(name, description) VALUES (?, ?)', (project_name, project_description))
    connect().commit()

    return cursor.lastrowid


def add_asset(group_id=None):
    if group_id is None:
        raise ValueError('No project id defined')

    cursor = connect().cursor()
    cursor.execute('INSERT INTO assets(id_group) VALUES (?)', (group_id,))
    connect().commit()

    return cursor.lastrowid
