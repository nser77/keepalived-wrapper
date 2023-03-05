import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name="keepalived-wrapper",
    version="0.0.1",
    packages=find_packages(),
    url="https://github.com/nser77/keepalived-wrapper",
    license="MIT",
    long_description=long_description,
    author="KimiNewt",
    description="Python wrapper for Keepalived",
    keywords="keepalived python wrapper",

    classifiers=[
        'License :: MIT License',
    ],
)
