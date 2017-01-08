from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='koalas',
    version='0.0.1',
    description='',
    url='https://github.com/',
    author='l',
    author_email='l@l.ca',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'pandas.ext': [
            'koalas = koalas',
        ],
    },
)
