from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import pyhelloworld

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='pyhelloworld',
    version=pyhelloworld.__version__,
    url='http://github.com/jripsl/pyhelloworld/',
    license='Apache Software License',
    author='jripsl',
    tests_require=['pytest'],
    install_requires=['colorise>=0.1.4'],
    cmdclass={'test': PyTest},
    author_email='jripsl@outlook.com',
    description='Python project template printing Hello world',
    long_description=long_description,
    packages=['pyhelloworld'],
    include_package_data=True,
    platforms='any',
    test_suite='pyhelloworld.test.test_pyhelloworld',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
