# Inflam

![Continuous Integration build in GitHub Actions](https://github.com/hangqianjun/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation/deployment

After cloning the repository ([download](https://github.com/hangqianjun/python-intermediate-inflammation.git)) the attached requirements file can be used to install dependencies with:

> $ pip3 install -r requirements.txt

## Basic usage

To view data in a csv file, call the inflamation-analysis python file with --view record option, for the patient you would like view, and with a pointer to the csv file containing the data.

> python3 inflammation-analysis.py --view record --patient 1 data/inflammation-01.csv

## Credits/Acknowledgements

This software was created via the Carpentries Incubator project: [Intermediate Research Software Development in Python](https://github.com/carpentries-incubator/python-intermediate-development).

## Licence

The software is available under a MIT licence.
