#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-style-darcula',
    version='0.1',
    description='Pygments version of JetBrains darcula theme.',
    license='BSD',
    author='Thibaud Lepretre',
    author_email='thibaud.lepretre@gmail.com',
    keywords=['pygments', 'style', 'dark', 'syntax highlighting'],

    url='https://github.com/kakawait/pygments-darcula',

    packages = find_packages(),
    install_requires=['pygments >= 1.5'],

    entry_points='''
    [pygments.styles]
    darcula=pygments_style_darcula:DarculaStyle
    darcula_properties=pygments_style_darcula:DarculaPropertiesStyle
    ''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)