#!/usr/bin/env python

"""The setup script."""

import pathlib
from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

readme = pathlib.Path('README.md').read_text()

setup(
    author="Panos Stavrianos",
    author_email='panos@orbitsystems.gr',
    python_requires='>=3.6',
    description="A simple component to add a timer to your flet app!",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords=['flet', 'flet_timer', 'timer', 'flet app', 'flet components','python','gui','ui'],
    name='flet_timer',
    packages=find_packages(include=['flet_timer', 'flet_timer.*']),
    url='https://github.com/panos-stavrianos/flet_timer',
    version='{{VERSION_PLACEHOLDER}}',
    zip_safe=False,
)
