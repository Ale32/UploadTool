__author__ = 'a.paoletti'

import sqlite3

conn = sqlite3.connect("example.db")

textures_dict = (
    "normal",
    "diffuse",
    "roughness",
    "specular",
    "occlusion",
    "metallic",
    "albedo",
    "color"
)


def get_projects():
    pass


def get_assets(project):
    pass


def check_texture_type():
    pass