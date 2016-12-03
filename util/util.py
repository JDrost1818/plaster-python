import os


def create_file(path, name, file_contents, create_not_found_dirs=True, mode="w+"):
    if create_not_found_dirs and not os.path.isdir(path):
        os.makedirs(path)

    file = open(os.path.join(path, name), mode)
    file.write(file_contents)
    file.close()


def type_to_var(type):
    return type[0].lower() + type[1:]
