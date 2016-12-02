_template = """
package {package};

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.data.repository.CrudRepository;

import com.{model_package}.{model};

public interface {repo_name} extends CrudRepository<{model}, {id_type}> {{

    List<{model}> findAll(Specification<{model}> spec);

    {model} findOne(Specification<{model}> spec);


}}
"""


def gen_contents(package, repo_name, model_package, model_name, id_type='Integer'):
    return _template.format(
        package=package,
        model_package=model_package,
        model=model_name,
        id_type=id_type,
        repo_name=repo_name)
