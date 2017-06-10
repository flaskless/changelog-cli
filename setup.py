from setuptools import setup, find_packages
import os

VERSION_FILE = 'src/changelog/_version.py'
with open(VERSION_FILE, 'r') as vf:
    value = vf.read()
v = value.split('=')[1].strip().strip('"')

dev_requirements = [
    'prospector',
    'tox',
    'twine',
    'coverage',
    'invoke',
    'wheel',
]

setup(
    name='changelog-cli',
    description='Command line interface for managing CHANGELOG.md files',
    long_description=open("README.md").read(),
    version=os.getenv('MODULE_VERSION_ID', v),
    author='Ryan McDevitt',
    author_email='mcdevitt.ryan@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mc706/changelog-cli',
    install_requires=[
        'click'
    ],
    extras_require={'dev': dev_requirements},
    entry_points={
        'console_scripts': [
            'changelog=changelog.commands:cli',
            'cl=changelog.commands:cli'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Documentation',
        'Topic :: Utilities',
    ]
)
