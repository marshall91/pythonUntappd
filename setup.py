#!/usr/bin/env python

from distutils.core import setup

long_description = open('README').read()

setup(
    name='pythonUntappd',
    version="0.1",
    py_modules = ['pytappd'],
    description='A python library to wrap the Untappd.com API',
    author='Mackenzie Marshall',
    author_email='mack.j.marshall@gmail.com',
    license='BSD License',
    url='http://github.com/marshall91/pythonUntappd',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)