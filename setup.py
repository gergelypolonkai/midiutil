import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='MIDIUtil',
    version='0.87',
    description='MIDIUtil, a MIDI Interface for Python',
    author='Mark Conway Wirt',
    author_email='emergentmusics) at (gmail . com',
    url='http://www.emergentmusics.org/midiutil/',
    license='Copyright (C) 2009, Mark Conway Wirt. See License.txt for details.',
    packages=['midiutil'],
    package_dir = {'midiutil': 'src/midiutil'},
    package_data={'midiutil' : ['../../documentation/*']},
    scripts=['examples/single-note-example.py'],
    long_description='''
This package provides a simple interface to allow Python programs to
write multi-track MIDI files.''',
    classifiers=[
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
        ]
)
