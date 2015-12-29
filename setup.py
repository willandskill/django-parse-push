# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-parse-push',
    version='0.0.1',
    author=u'Will & Skill AB',
    author_email='info@willandskill.se',
    packages=find_packages(),
    url='https://github.com/willandskill/django-parse-push',
    license='BSD licence, see LICENCE.txt',
    description='Simple Django based wrapper for Parse Push API',
    long_description=open('README.md').read(),
    zip_safe=False,
    # test_suite="testproject.runtests.runtests",
)