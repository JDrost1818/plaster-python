import pattern.text.en as pattern

import data.types as gen_types
import template.model.model as model_file_gen
import template.repository as repo_file_gen
from domain.file_information import FileInformation
from util.util import *

_generation_map = {
    'scaffold': [
        gen_types.MODEL,
        gen_types.REPOSITORY
    ]
}

_template_map = {
    gen_types.MODEL: model_file_gen,
    gen_types.REPOSITORY: repo_file_gen
}


def generate_repository(rel_path, maven_group_id, gen_name, fields, type):
    """
    Facilitates the necessary information to create a file and populate a template for a repository

    :param rel_path:
    :param maven_group_id:
    :param gen_name:
    :param fields:
    :param type:
    :return:
    """

    # transforms the given information into specialized
    # info which will be used to create the file
    package = gen_repo_package(maven_group_id)
    class_name = gen_name + 'Repository'
    filename = class_name + '.java'
    rel_path = gen_repo_path(rel_path, maven_group_id)
    model_package = gen_model_package(maven_group_id)

    # generates the file contents and then creates the file
    file_contents = repo_file_gen.gen_contents(package, class_name, model_package, gen_name)
    create_file(rel_path, filename, file_contents)


def generate_service(rel_path, maven_group_id, gen_name, fields, type):
    print 'Generating service at :', gen_path(rel_path, maven_group_id) + gen_name + "Service.java"


def generate_controller(rel_path, maven_group_id, gen_name, fields, type):
    rel_path = gen_path(rel_path, maven_group_id)
    filename = gen_name + 'sController.java'

    print 'Generating controller at :', rel_path + filename


def generate_file(file_info):
    template = _template_map[file_info.file_type]

    file_contents = template.gen_contents(file_info)
    create_file(file_info.file_path, file_info.file_name, file_contents)


def perform(gen_type, gen_name, fields):
    generations = _generation_map[gen_type]

    if not (gen_name and gen_type):
        return "Missing required argument"
    if not generations:
        return "Unknown generation type :", gen_type

    gen_name = pattern.singularize(gen_name.capitalize().replace(' ', ''))
    files_to_generate = [FileInformation(gen_name, fields, elem) for elem in generations]
    for file_to_generate in files_to_generate:
        generate_file(file_to_generate)
