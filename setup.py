# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='django-session-cleanup',
    version='0.0.2',
    description=('A periodic task for removing expired Django sessions '
                 'from the django_session table'),
    long_description=readme,
    author='Elijah Rutschman',
    author_email='elijahr+django-session-cleanup@gmail.com',
    maintainer='Martey Dodoo',
    maintainer_email='martey+django-session-cleanup@mobolic.com',
    url='https://github.com/sandersnewmedia/django-session-cleanup',
    license=license,
    packages=find_packages(exclude=('tests',))
)
