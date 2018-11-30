#!/usr/bin/env python
import os
from setuptools import setup

rootdir = os.path.abspath(os.path.dirname(__file__))
name = "texttv"
long_description = open(os.path.join(rootdir, 'README.md')).read().strip()
VERSION = open(os.path.join(rootdir, 'VERSION')).read().strip()


setup(
    name='python-' + name,
    version=VERSION,
    description='texttv',
    long_description=long_description,
    url='',
    author='gardsted',
    author_email='gardsted@gmail.com',
    license='MPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: Mozilla Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mail',
    packages=["texttv"]
)
