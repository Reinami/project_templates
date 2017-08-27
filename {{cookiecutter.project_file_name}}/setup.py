import codecs
import os
import re
from setuptools import setup


with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), '{{cookiecutter.project_file_name}}', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name='{{cookiecutter.project_file_name}}',
    version=version,
    url='http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_file_name}}',
    license='MIT',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    description='{{cookiecutter.project_description}}',
    packages=['{{cookiecutter.project_file_name}}'],
    platforms='any',
    install_requires=[
        
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)