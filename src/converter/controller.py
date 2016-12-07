import pattern.text.en as pattern

import src.data.settings as settings
from src.data.types import CONTROLLER as GEN_TYPE


def gen_root_name(root_name):
    return pattern.pluralize(root_name)


def gen_package_name():
    return settings.MAVEN_GROUP_ID + '.' + settings.RELATIVE_PACKAGES[GEN_TYPE]


def gen_class_name(root_name):
    return gen_root_name(root_name) + 'Controller'


def gen_file_path():
    return settings.REL_PATH + settings.RELATIVE_PACKAGES[GEN_TYPE]


def gen_file_name(root_name):
    return gen_class_name(root_name) + '.java'
