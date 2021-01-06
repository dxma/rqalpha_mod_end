# -*- coding: utf-8 -*-
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='rqalpha-mod-end',
    version='0.0.1',
    description='rqalpha-mod-end',
    packages=find_packages(exclude=[]),
    author='dxma',
    author_email='dongxu.ma@gmail.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    install_requires=[
    ],
    zip_safe=False,
)
