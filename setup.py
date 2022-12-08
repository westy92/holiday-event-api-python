import sys
from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

# TODO test on 3.5 or 2.7
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write('holiday-event-api requires Python version {}.{} or higher.'
        .format(*(CURRENT_PYTHON)))
    sys.exit(1)

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='holiday-event-api',
    version='0.0.1',
    description='The Official Holiday and Event API for Python',
    long_description_content_type='text/markdown',
    long_description=readme,
    url='https://pypi.org/project/holiday-event-api/',
    author='Seth Westphal',
    author_email='seth@sethwestphal.com',
    maintainer='Seth Westphal',
    keywords=['python','holiday','api'], # TODO
    license='MIT',
    packages=['holidays'],
    python_requires='>=3.7, <4',
    install_requires=[
        'requests>=2, <3',
    ],
    classifiers=[
        # TODO audit these. Add more?
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        #'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        #'Programming Language :: Python :: Implementation :: CPython',
        #'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        # 'Topic :: Utilities',
    ],
)