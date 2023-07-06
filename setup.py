#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

setup(
    author="Panos Stavrianos",
    author_email='panos@orbitsystems.gr',
    python_requires='>=3.6',
    description="A simple component to add a timer to your flet app",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='flet_timer',
    name='flet_timer',
    packages=find_packages(include=['flet_timer', 'flet_timer.*']),
    url='https://github.com/panos-stavrianos/flet_timer',
    version='0.0.1',
    zip_safe=False,
)
