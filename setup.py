# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name='aiohttp_client_manager',
    description='Automatic aiohttp ClientSession management',
    keywords='aiohttp client session management',
    author='Nathan Van Gheem',
    author_email='vangheem@gmail.com',
    version=open('VERSION').read().strip(),
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGELOG.rst').read()),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url='https://pypi.python.org/pypi/aiohttp_client_manager',
    license='GPL version 3',
    setup_requires=[
        'pytest-runner',
        'lru-dict',
        'aiohttp'
    ],
    zip_safe=True,
    include_package_data=True,
    py_modules=['aiohttp_client'],
    install_requires=[],
    tests_require=[],
)
