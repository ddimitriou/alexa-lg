from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version_regex = re.compile(r'__version__ = [\'\"]v((\d+\.?)+)[\'\"]')
with open('src/AlexaLG/__init__.py') as f:
    vlines = f.readlines()
__version__ = next(re.match(version_regex, line).group(1) for line in vlines
                   if re.match(version_regex, line))

setup(
    name='alexa-lg',
    version=__version__,
    description='LG TV Controls with Alexa',
    long_description=long_description,
    url='https://github.com/ddimitriou/alexa-lg',
    author='Dimitri Dimtiriou',
    author_email='dimitriou.d.a@gmail.com',
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6"
    ],
    keywords='fauxmo alexa lg-smart-tv',
    packages=find_packages(where='./', exclude=['contrib', 'docs', 'tests']),
    install_requires=['fauxmo', 'LGWebOSRemote'],
    extras_require={},
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'AlexaLG=AlexaLG:run',
        ],
    },
)
