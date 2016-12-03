from current import TEMPLATE as BASE

_lombok_header = """import lombok.Data;
{header}
@Data"""

TEMPLATE = BASE.replace('{header}', _lombok_header)
