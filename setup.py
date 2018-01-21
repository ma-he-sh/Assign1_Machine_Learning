# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

config = {
    'description': 'scraping for bitcoin history',
    'author': 'Mahesh Ranaweera',
    'author_email': 'mahesh.ranaweerakaluarachchige@uoit.net',
    'version': '0.0.1',
    'packages': find_packages(),
    'url': 'https://github.com/Mahesh-Ranaweera/Assign1_SOFE4620U',
    'name': 'scrapebc',
    'long_description': readme
}

setup(**config)