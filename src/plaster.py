#!/usr/bin/python

import argparse
import os
import sys
from argparse import RawTextHelpFormatter

import src.data.settings as settings
import src.generation.generator as generator
from data.strings import Docs
from data.version import __version__

generators = {
    'g': generator,
    'generate': generator
}


def main():
    parser = argparse.ArgumentParser(
        prog='plaster',
        description='Generate files for Spring Boot',
        formatter_class=RawTextHelpFormatter)

    # Positional Arguments
    parser.add_argument('-v', '--version', help=Docs.version, action='version', version=__version__)
    parser.add_argument('-k', '--key', nargs='?', help=Docs.key)

    parser.add_argument('mode', choices=Docs.generation_mode_choices, help=Docs.generation_mode)
    parser.add_argument('type', choices=Docs.generation_type_choices, help=Docs.generation_type)
    parser.add_argument('model', help=Docs.model)
    parser.add_argument('fields', nargs='*', help=Docs.fields)

    args = parser.parse_args()

    print args

    if len(sys.argv) < 2:
        print 'USAGE: plaster <type> [field:type]*'
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


if __name__ == '__main__':
    main()
