from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='calculator',
    version='0.1.0',
    description='Simple calculator',
    long_description=readme,
    author='Akshay',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)