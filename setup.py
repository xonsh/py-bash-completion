#! /usr/bin/env python
import sys
try:
    from setuptools import setup
    HAVE_SETUPTOOLS = True
except ImportError:
    from distutils.core import setup
    HAVE_SETUPTOOLS = False


VERSION = '0.2.7'

setup_kwargs = {
    "version": VERSION,
    "description": ('Python interface for bash completion'),
    "license": 'BSD 3-clause',
    "author": 'The xonsh developers',
    "author_email": 'xonsh@googlegroups.com',
    "url": 'https://github.com/xonsh/py-bash-completion',
    "download_url": "https://github.com/xonsh/py-bash-completion/zipball/" + VERSION,
    "classifiers": [
        "License :: OSI Approved",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Utilities",
        ],
    "zip_safe": False,
    "data_files": [("", ['LICENSE', 'README.rst']),],
    }


if __name__ == '__main__':
    setup(
        name='bash_completion',
        py_modules=['bash_completion'],
        long_description=open('README.rst').read(),
        **setup_kwargs
)
