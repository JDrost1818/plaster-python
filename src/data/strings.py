class Docs:
    version = 'fetches the current version of the tool'

    generation_mode = 'whether to generate or delete\n' \
                      '    generate, g - create files\n' \
                      '    delete, d - remove files'

    generation_type = 'how to generate or delete content\n' \
                      '    scaffold - all files associated to the model\n' \
                      '    model - the entire model\n' \
                      '    repository - the entire repository\n' \
                      '    service - the entire service\n' \
                      '    controller - the entire controller\n' \
                      '    field - individual field(s)'

    model = 'name of model for which to perform actions'
