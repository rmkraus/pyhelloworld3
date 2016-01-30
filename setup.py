from setuptools import setup
import pyhelloworld3

setup(
    name='pyhelloworld3',
    version=pyhelloworld3.__version__,
    url='http://github.com/rmkraus/pyhelloworld3/',
    license='Apache Software License',
    author='rmkraus',
    description='Hello world',
    long_description="Smallest package ever"
    "Useful for testing automated package management",
    packages=['pyhelloworld3'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python 3',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
