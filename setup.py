from os.path import join
from glob import glob

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dominionSolver",
    version="0.0.1",
    author="Bailey Painter",
    author_email="bpainter6@gatech.edu",
    description="Package for reading and analyzing stock data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bpainter6/dominion-solver",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=['dominionSolver', 'dominionSolver.checkerrors', 
              'dominionSolver.functions', 'dominionSolver.objects'],
)
