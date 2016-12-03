import data.java_types as java_type_converter

_template = '''package {package};

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.Data;

@Data
@Entity
public class {class_name} {{

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private {id_type} id;
'''

_field_template = '''
    private {type} {name};
'''


def gen_contents(file_info, id_type='Integer'):
    file_contents = _template.format(
        package=file_info.package,
        class_name=file_info.class_name,
        id_type=id_type)

    for field in file_info.fields:
        name, field_type = field.split(':')

        field_type = java_type_converter.translate_type(field_type)
        if field_type:
            file_contents += _field_template.format(type=field_type, name=name)

    return file_contents + "}\n"
