import data.strategy as gen_stategies
import data.types as gen_types
import templates.model as model_file_gen
import templates.repository as repo_file_gen
from util.util import *


def generate_model(rel_path, maven_group_id, gen_name, fields, type):
    """
    Facilitates the necessary information to create a file and populate a template for a model

    :param rel_path:
    :param maven_group_id:
    :param gen_name:
    :param fields:
    :param type:
    :return:
    """
    package = gen_model_package(maven_group_id)
    class_name = gen_name
    filename = class_name + '.java'
    rel_path = gen_model_path(rel_path, maven_group_id)

    file_contents = model_file_gen.gen_contents(package, class_name, fields)
    create_file(rel_path, filename, file_contents)


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


_generation_map = {
    'scaffold': [
        gen_types.CONTROLLER,
        gen_types.SERVICE,
        gen_types.REPOSITORY,
        gen_types.MODEL
    ]
}

_gen_function_map = {
    gen_types.CONTROLLER: generate_controller,
    gen_types.SERVICE: generate_service,
    gen_types.REPOSITORY: generate_repository,
    gen_types.MODEL: generate_model
}


def perform(rel_path, maven_group_id, gen_type, gen_name, fields):
    """

    :param gen_path: String - root to root level of the maven project (where to gen files)
    :param gen_type: String - type of generation to do. See generation_types
    :param gen_name: String - name to base the files off of
    :param fields: [String:String] - field names to generate for the files
    :return: error msg if one occurs, otherwise, None
    """
    generations = _generation_map[gen_type]

    if not (gen_name and gen_type):
        return "Missing required argument"
    if not generations:
        return "Unknown generation type :", gen_type

    gen_name = gen_name.capitalize().replace(' ', '')

    for gen in generations:
        _gen_function_map[gen](rel_path, maven_group_id, gen_name, fields, gen_stategies.GENERATE)
