from data.java_types import translate_type


class Field:
    def __init__(self, name_or_name_type_pair, field_type=None):
        if not field_type:
            # this means we were passed in a name-type pair
            self.name, self.field_type = name_or_name_type_pair.split(':')
        else:
            # this means we were passed both args
            self.name = name_or_name_type_pair
            self.field_type = field_type

        self.field_type = translate_type(self.field_type)

    def __str__(self):
        return '%s %s' % (str(self.field_type), str(self.name))
