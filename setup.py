import os
from setuptools import setup


def read_(fname):
    """
    Utility function to read the README file
    Easier than line wrapping a long string...
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="quickpin_api",
    version="0.0.2",
    author="Luke Maxwell",
    author_email="lukemaxwellshouse@gmail.com",
    description=("A python wrapper for the QuickPin API."),
    license="BSD",
    keywords="python, quickpin, api",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['quickpin_api'],
    include_package_data=True,
    install_requires=[
        'requests',
        'click',
        'sseclient'
    ],
    entry_points={
        'console_scripts': ['quickpin=quickpin_api.qpi:cli'],
    },
    scripts=[],
    long_description=read_('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: QuickPin, Social Media, Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
