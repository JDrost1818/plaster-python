_template = """package {package};

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.data.repository.CrudRepository;

import {model_package}.{model};

public interface {class_name} extends CrudRepository<{model}, {id_type}> {{

    Page<{model}> findAll(Specification<{model}> spec, Pageable pageInfo);

    {model} findOne(Specification<{model}> spec);


}}
"""


def gen_contents(package, class_name, model_package, model_name, id_type='Integer'):
    return _template.format(
        package=package,
        class_name=class_name,
        model_package=model_package,
        model=model_name,
        id_type=id_type)
