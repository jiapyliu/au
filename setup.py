import sys
import os
from setuptools import setup,find_packages
import pprint

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here,'au','__version__.py'),'r',encoding='utf-8') as f:
    exec (f.read(),about)

packages = ['au','au.*']
# requires = [
#
# ]
#
setup(
    name = 'au',
    packages = find_packages(include=packages),
    version=about['__version__'],
    description=about['__description__'],

    project_urls={
        'Documentation': 'https://github.com/jiapyliu/au',
        'Source': 'https://github.com/jiapyliu/au',
    },
)