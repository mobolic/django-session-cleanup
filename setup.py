# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='django-session-cleanup',
    version='1.0.0',
    description=('A periodic task for removing expired Django sessions '
                 'with Celery.'),
    long_description=readme,
    author='Elijah Rutschman',
    author_email='elijahr+django-session-cleanup@gmail.com',
    maintainer='Martey Dodoo',
    maintainer_email='martey+django-session-cleanup@mobolic.com',
    url='https://github.com/sandersnewmedia/django-session-cleanup',
    classifiers=[
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=('tests',))
)
