import re

import src.util.util as util

_dependency_template = 'import {dep};\n'


def format_template(content):
    return remove_multiple_newlines(content)


def remove_multiple_newlines(content):
    return re.sub(r'(\n\n\n)+', r'\n', content)


def gen_dependency_string_for_field(fields):
    """
    Gets all the dependencies frome the fields and flattens that list of dependencies.
    Example:
        fields = [Field::[dep1, dep2], Field[dep3], ... , Field[depN] => [dep1, dep2, dep3, ... , depN]

    Then uses these dependencies to create Java import statements

    :param fields: the fields which may or may not have dependencies
    :return:
    """
    fields_with_dependencies = [field for field in fields if field.field_type.has_dependency()]
    dependencies_list = [field.field_type.dependencies for field in fields_with_dependencies]
    dependencies = util.flatten(dependencies_list)

    return gen_dependency_string(dependencies)


def gen_dependency_string(dependencies):
    # Finds all the dependencies needed for the fields
    unique_deps = list(set(dependencies))

    return ''.join([_dependency_template.format(dep=dep) for dep in unique_deps])
