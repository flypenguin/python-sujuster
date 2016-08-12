#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

import io


VERSION = "1.0.1"


install_reqs = parse_requirements("./requirements.txt", session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]

long_description = (
    io.open('README.rst', encoding='utf-8').read() +
    '\n' +
    io.open('CHANGES.rst', encoding='utf-8').read()
)

setup(
    name             = 'sujuster',
    packages         = find_packages(),
    version          = VERSION,
    description      = 'The SUbtitle adJUSTER - '
                       'adjust offsets of a .srt subtitle file',
    long_description = long_description,
    author           = 'Axel Bock',
    author_email     = 'mr.axel.bock@gmail.com',
    url              = 'https://github.com/flypenguin/python-sujuster',
    download_url     = 'https://github.com/flypenguin/python-sujuster/tarball/{}'.format(VERSION),
    keywords         = 'subtitles srt script',
    install_requires = reqs,
    entry_points     = {
        'console_scripts': [
            'sujuster=sujust:console_entrypoint',
        ],
    },
    classifiers      = [
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Topic :: System :: Systems Administration",
        "Topic :: Software Development :: Testing",
    ],
)