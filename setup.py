#!/usr/bin/env python

import os.path
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    sys.exit()

description = 'Google Spreadsheets Python API'

long_description = """
{index}

License
-------
MIT
"""

setup(
    name='aiospread',
    packages=['aiospread'],
    description=description,
    long_description=long_description,
    version='1.0.0',
    author='Anton Burnashev',
    author_email='fuss.here@gmail.com',
    url='https://github.com/RainbowLegend/aiospread',
    keywords=['spreadsheets', 'google-spreadsheets', 'asyncio'],
    install_requires=['aiohttp'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    license='MIT'
    )
