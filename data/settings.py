import types as types

BASE_PATH = 'src/main/java/'
REL_PATH = ''
MAVEN_GROUP_ID = ''

IS_LOMBOK_SUPPORTED = False

RELATIVE_PACKAGES = {
    types.MODEL: 'model',
    types.REPOSITORY: 'repository',
    types.SERVICE: 'service',
    types.CONTROLLER: 'controller',
}


def load(xml_tree):
    global REL_PATH, MAVEN_GROUP_ID, IS_LOMBOK_SUPPORTED

    # Everything is prepended with this version,
    # so lets get it so we can use it down the line
    version = xml_tree.tag.replace('project', '')

    MAVEN_GROUP_ID = xml_tree.find(version + 'groupId').text
    REL_PATH = BASE_PATH + MAVEN_GROUP_ID.replace('.', '/') + '/'

    dependencies = xml_tree.find(version + 'dependencies')

    # The generation can behave differently based on dependencies in the project
    # The searches being performed her are the following:
    #
    #       Lombok
    #           - We don't have to define getters and setters when generating model
    #
    if len(dependencies) != 0:
        for dependency in dependencies.findall(version + 'dependency'):
            if dependency.find(version + 'artifactId').text == 'lombok':
                IS_LOMBOK_SUPPORTED = True
