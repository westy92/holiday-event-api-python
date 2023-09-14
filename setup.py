import sys
from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 8)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        'holiday-event-api requires Python version {}.{} or higher.'
        .format(*(CURRENT_PYTHON)))
    sys.exit(1)

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='holiday-event-api',
    version='1.0.1',
    description='The Official Holiday and Event API for Python',
    long_description_content_type='text/markdown',
    long_description=readme,
    url='https://github.com/westy92/holiday-event-api-python',
    project_urls={
        'Documentation': 'https://github.com/westy92/holiday-event-api-python',
        'Releases': 'https://github.com/westy92/holiday-event-api-python/releases',
        'Issues': 'https://github.com/westy92/holiday-event-api-python/issues',
        'Funding': 'https://github.com/sponsors/westy92',
    },
    author='Seth Westphal',
    author_email='seth@sethwestphal.com',
    maintainer='Seth Westphal',
    keywords=[
        'python',
        'holiday',
        'holidays',
        'public',
        'federal',
        'official',
        'unofficial',
        'date',
        'month',
        'year',
        'day',
        'calendar',
        'api',
        'holidayapi',
        'list',
        'event',
        'occurrence',
        'celebration',
        'description',
        'details',
        'checkiday',
        'international',
        'national',
        'world',
        'popular',
        'trusted',
        'accurate',
        'free',
        'best',
    ],
    license='MIT',
    license_file='LICENSE',
    packages=['holidays'],
    python_requires='>=3.8, <4',
    install_requires=[
        'requests>=2, <3',
        'marshmallow_dataclass>=8',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)
