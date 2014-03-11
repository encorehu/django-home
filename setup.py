#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='home',
    version="0.1",
    author='encorehu',
    author_email='huyoo353@126.com',
    description='a django project specific app.',
    url='https://github.com/encorehu/django-home',
    packages=find_packages(),
    package_dir={'home':'home'},
    package_data={'home':['*.*','templates/home/*.*']},
    zip_safe = False,
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
