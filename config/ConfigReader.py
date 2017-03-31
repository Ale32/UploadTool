import json
import os

config_data = None


def read_config():
    global config_data

    if config_data is not None:
        return config_data

    config_file = os.path.join('config', 'config.json')
    config_file = os.path.abspath(config_file)

    with open(config_file) as f:
        config_data = json.load(f)

    return config_data


def db_path():
    config_data = read_config()

    if not config_data['paths']['database']:
        return 'database.db'

    return config_data['paths']['database']


def accepted_format(filename, file_type):
    config_data = read_config()
    ext = os.path.splitext(filename)[1].replace('.', '')

    if ext.lower() in [format.lower() for format in config_data['file_formats'][file_type]]:
        return True

    return False


def accepted_textures(filename):
    return accepted_format(filename, 'texture')


def accepted_files(filename):
    return accepted_format(filename, 'file')


def generate_file_filter():
    config_data = read_config()
    file_formats = ['*.{}'.format(f.lower()) for f in config_data['file_formats']['file']]
    return ' '.join(file_formats)


def generate_texture_filter():
    config_data = read_config()
    file_formats = ['*.{}'.format(f.lower()) for f in config_data['file_formats']['texture']]
    return ' '.join(file_formats)
