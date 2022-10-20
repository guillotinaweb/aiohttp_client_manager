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
    license='BSD',
    zip_safe=True,
    include_package_data=True,
    py_modules=['aiohttp_client'],
    install_requires=[
        'lru-dict',
        'aiohttp'
    ],
    extras_require={
        'test': [
            'pytest==4.4.0',
            'pytest-runner',
            'pytest-aiohttp',
            'pytest-asyncio',
            'attrs>=19.1.0'
        ]
    }
)
