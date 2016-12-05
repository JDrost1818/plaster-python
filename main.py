#!/usr/bin/python

"""
To use this generation utility you must subscribe to a few naming conventions:

    Note: generating "user"

    Type       : Folder               : Filename
    ------------------------
    Controller : src/main/{maven-groupId}/controller/ : UsersController
    Service    : src/main/{maven-groupId}/service/    : UserService
    Repository : src/main/{maven-groupId}/repository/ : UserRepository

    There is currently no way to change these defaults
"""

import os
import sys

import data.settings as settings
import generation.generator as generator

generators = {
    'g': generator,
    'generate': generator
}

if len(sys.argv) < 2:
    print 'USAGE: python main.py <type>'
    sys.exit(-1)
if not os.path.isfile('./pom.xml'):
    print 'Not on the root level of a maven project - cannot generate'
    sys.exit(-1)

args = sys.argv[1:]

gen_type = args[0].lower()
gen_sub_type = args[1].lower()
gen_name = args[2].lower()
gen_kwargs = args[3:]

settings.load()

error = generators[gen_type].perform(gen_sub_type, gen_name, gen_kwargs)

if error:
    print error
