import json
import os

config_data = None


class ConfigException(Exception):
    pass


def read_config():
    global config_data

    if config_data is not None:
        return config_data

    config_file = os.path.join(os.path.dirname(__file__), 'config.json')
    config_file = os.path.abspath(config_file)

    with open(config_file) as f:
        config_data = json.load(f)

    return config_data


def db_path():
    config_data = read_config()

    database = config_data['paths']['database']
    if not database:
        raise ConfigException("Missing database path in config file!")

    return database


def server_name():
    config_data = read_config()

    server = config_data['paths']['server']
    if not server:
        raise ConfigException("Missing server name in config file!")

    return server


def share_name():
    config_data = read_config()

    share = config_data['paths']['share']
    if not share:
        raise ConfigException("Missing share name in config file!")

    return share


def content_name():
    config_data = read_config()

    content = config_data['paths']['content']
    if not content:
        raise ConfigException("Missing content name in config file!")

    return content


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
    file_formats = ['*.{}'.format(f.lower()) for f in config_data['file_formats']['meshes']]
    return ' '.join(file_formats)


def generate_texture_filter():
    config_data = read_config()
    file_formats = ['*.{}'.format(f.lower()) for f in config_data['file_formats']['textures']]
    return ' '.join(file_formats)


def asset_prefix(asset_type):
    config_data = read_config()

    prefix = config_data['asset_prefix'][asset_type]
    if not prefix:
        raise ConfigException("Missing asset prefix in config file!")

    return prefix


def texture_suffix(filename):
    """
    Take last piece of filename (character between last _ and extension)
    and check if it is a known texture type from config file.

    Example1: assetname_diffuse.png ---> _D
    Example2: assetname_diffuse01.png ---> _D01

    :param filename: name of file
    :return: texture suffix + texture number (from file)
    """
    config_data = read_config()

    filename = os.path.splitext(filename)[0]
    txt_part = filename.split("_")[-1]

    txt_number = ''
    if len(txt_part) > 2:
        txt_number = txt_part[-2:] if txt_part[-2:].isdigit() else ''

    if txt_number:
        txt_part = txt_part[:-2]

    for txt_type in config_data['texture_naming']:
        if txt_part in config_data['texture_naming'][txt_type]['text']:
            return config_data['texture_naming'][txt_type]['suffix'] + txt_number

    return None


def file_type_from_ext(ext):
    config_data = read_config()

    for file_type in config_data['file_formats']:
        if ext.lower() in config_data['file_formats'][file_type]:
            return file_type

    return None


def texture_naming_dict():
    config_data = read_config()

    return config_data['texture_naming']
