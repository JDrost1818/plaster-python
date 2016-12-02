STRING = 'String'
INTEGER = 'Integer'

types = {
    'string': STRING,
    'int': INTEGER,
    'integer': INTEGER
}


def translate_type(type):
    return types[type.lower()]
