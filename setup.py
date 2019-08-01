#!/usr/bin/env python
from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    
setup(name='gcc-tree-explorer',
      version='0.1.0',
      install_reqs = parse_requirements('requirements.txt', session='hack'),
      packages=find_packages())
