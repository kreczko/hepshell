#!/usr/bin/env python

from distutils.core import setup

setup(
    name='hepshell',
    version='0.1.0',
    description='A Python Shell for High Energy Particle Physics',
    author='Luke Kreczko',
    author_email='lkreczko@gmail.com',
    packages=['hepshell', 'hepshell.commands'],
)
