from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='nexo-webapp',
    version='1.0.0',
    description='Flask application for Nexo Ecosystem',
    long_description=readme,
    author='Angel Rojo',
    url='https://github.com/ilittleangel/nexo-webapp',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['flask', 'werkzeug', 'click']
)
