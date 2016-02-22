import os
from setuptools import find_packages, setup

root = os.path.dirname(os.path.realpath(__file__))
long_description = open(os.path.join(root, 'README.md')).read()

setup(
    name='range-glob',
    version='1.0.0',
    description='Python numeric range glob expression generator',
    long_description=long_description,
    url='http://github.com/artirix/range-glob',
    author='Robin Hughes',
    author_email='robin.hughes@artirix.com',
    license='BSD',
    # packages=['range_glob'],
    packages=find_packages(),
    include_package_data=True,
    keywords='numeric range glob expression generator',
)
