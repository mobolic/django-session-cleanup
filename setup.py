# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='django-session-cleanup',
    version='4.0.0',
    description=('A periodic task for removing expired Django sessions '
                 'with Celery.'),
    long_description=readme,
    author='Elijah Rutschman',
    author_email='elijahr+django-session-cleanup@gmail.com',
    maintainer='Martey Dodoo',
    maintainer_email='martey+django-session-cleanup@mobolic.com',
    url='https://github.com/mobolic/django-session-cleanup',
    classifiers=[
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(exclude=('tests',))
)
