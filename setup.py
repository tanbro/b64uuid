#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup


def read_requires_file(file_name):
    return [
        line for line in map(lambda s: s.strip(), open(file_name, encoding='utf-8'))
        if line and not line.startswith('#')
    ]


setup(
    name='b64uuid',
    description='A small library and tool to encode/decode a python UUID object to/from a 22 characters length url safe base64 string.',  # noqa
    url='https://github.com/tanbro/b64uuid',
    author='liu xue yan',
    author_email='liu_xue_yan@foxmail.com',
    long_description=('{0}---{0}'.format(os.linesep * 2)).join(
        open(file, encoding='utf-8').read().strip()
        for file in ('README.md', 'CONTRIBUTING.md', 'CHANGELOG.md', 'AUTHORS.md')
    ),
    long_description_content_type='text/markdown',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.5',

    install_requires=read_requires_file('requirements.txt'),
    extras_require={},

    setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],

    use_scm_version={
        # guess-next-dev:	automatically guesses the next development version (default)
        # post-release:	generates post release versions (adds postN)
        'version_scheme': 'guess-next-dev',
        'write_to': 'src/b64uuid/version.py',
    },

    entry_points={
        'console_scripts': [
            'b64uuid = b64uuid.__main__:main',
        ],
    },
)
