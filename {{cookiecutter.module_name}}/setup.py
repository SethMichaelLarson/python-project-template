import os
import re
from setuptools import setup, find_packages

base_package = '{{cookiecutter.module_name}}'

# Get the version (borrowed from SQLAlchemy)
base_path = os.path.dirname(__file__)
with open(os.path.join(base_path, '{{cookiecutter.module_name}}', '__init__.py')) as f:
    module_content = f.read()
    VERSION = re.compile(r'.*__version__ = \'(.*?)\'', re.S).match(module_content).group(1)
    LICENSE = re.compile(r'.*__license__ = \'(.*?)\'', re.S).match(module_content).group(1)


with open('README.rst') as f:
    readme = f.read()

with open('CHANGELOG.rst') as f:
    changes = f.read()

with open('requirements.txt') as f:
    requirements = [line for line in f.read().split('\n') if len(line.strip())]


packages = find_packages(os.path.join(base_path, base_package))
if base_package not in packages:
    packages.append(base_package)


if __name__ == '__main__':
    setup(
        name='{{cookiecutter.module_name}}',
        description='{{cookiecutter.module_description}}',
        long_description='\n\n'.join([readme, changes]),
        license=LICENSE,
        url='http://{{cookiecutter.module_name}}.readthedocs.io',
        version=VERSION,
        author='{{cookiecutter.full_name}}',
        author_email='{{cookiecutter.email}}',
        maintainer='{{cookiecutter.full_name}}',
        maintainer_email='{{cookiecutter.email}}',
        install_requires=requirements,
        keywords=['{{cookiecutter.module_name}}'],
        packages=packages,
        zip_safe=False,
        classifiers=['Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7']
    )
