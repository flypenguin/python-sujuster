#!/usr/bin/env python

import io

from setuptools import setup, find_packages


VERSION = "1.0.4"

REQUIRED_PACKAGES = []


long_description = (
    io.open("README.rst", encoding="utf-8").read()
    + "\n"
    + io.open("CHANGES.rst", encoding="utf-8").read()
)

# fmt: off
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
    install_requires = REQUIRED_PACKAGES,
    entry_points     = {
        'console_scripts': [
            'sujust=sujuster:console_entrypoint',
        ],
    },
    classifiers      = [
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Topic :: Text Processing :: Filters",
        "Topic :: Utilities",
    ],
)
# fmt: on
