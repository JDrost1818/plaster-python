import data.java_types as JavaTypeConverter

_template = '''
package {package};

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.Data;

@Data
@Entity
public class {model} {{

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private {id_type} id;
'''

_field_template = '''
    private {type} {name};
'''


def gen_contents(package, model_package, model_name, fields, id_type='Integer'):
    file_contents = _template.format(
        package=package,
        model_package=model_package,
        model=model_name,
        id_type=id_type)

    for field in fields:
        name, field_type = field.split(':')

        field_type = JavaTypeConverter.translate_type(field_type)
        if field_type:
            file_contents += _field_template.format(type=field_type, name=name)

    return file_contents + "}}"
