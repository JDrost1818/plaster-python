import converter.model as model_converter
import converter.repository as repo_converter
import data.types as gen_types
from field import Field

file_converters = {
    gen_types.MODEL: model_converter,
    gen_types.REPOSITORY: repo_converter,
}


class FileInformation:
    def __init__(self, name, fields, file_type):
        converter = file_converters[file_type]
        if not converter:
            raise ValueError('Unsupported FileType :', file_type)

        self.package = converter.gen_package_name()
        self.class_name = converter.gen_class_name(name)
        self.model_package = converter.gen_model_package_name()
        self.model_name = converter.gen_model_name(name)
        self.file_path = converter.gen_file_path()
        self.file_name = converter.gen_file_name(name)
        self.file_type = file_type
        self.fields = [Field(name_pair) for name_pair in fields]

    def __str__(self):
        return '%s %s %s' % (str(self.file_type), str(self.package), str(self.class_name))
