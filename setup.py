#!/usr/bin/env python

from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session='hack')

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(name='tools',
      version='0.0.1',
      description='Tools',
      author='Daniel Suo',
      author_email='dsuo@cs.princeton.edu',
      url='https://github.com/danielsuo/tools',
      packages=['tools'],
      install_requires=reqs
      )
