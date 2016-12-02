import os


def create_file(path, name, create_not_found_dirs=True, mode="w+"):
    if create_not_found_dirs and not os.path.isdir(path):
        os.makedirs(path)

    return open(os.path.join(path, name), mode)


def gen_path(rel_path, maven_group_id):
    return rel_path + maven_group_id.replace('.', '/') + '/'


def gen_repo_path(rel_path, maven_group_id):
    return gen_path(rel_path, maven_group_id) + 'repository'


def gen_repo_package(maven_group_id, name=None):
    base = maven_group_id + '.' + 'repository'

    return base + '.' + name if name else base


def gen_model_package(maven_group_id, name=None):
    base = maven_group_id + '.' + 'model'

    return base + '.' + name if name else base
