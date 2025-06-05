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
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.1',
        'Framework :: Django :: 5.2',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    packages=find_packages(exclude=('tests',))
)
