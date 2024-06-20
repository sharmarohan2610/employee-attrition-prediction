# -*- coding: utf-8 -*-
"""setup.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AUUhiC46X0LZH59DaE5qJE89vZDOLwPW
"""

from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="employee-attrition-prediction",
    version="0.1.0",
    author="Rohan Sharma",
    author_email="sharmarohan2610@gmail.com",
    description="A machine learning project to predict employee attrition using regression techniques.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sharmarohan2610/employee-attrition-prediction",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas==1.3.3",
        "numpy==1.21.2",
        "matplotlib==3.4.3",
        "seaborn==0.11.2",
        "scikit-learn==0.24.2",
        "jupyter==1.0.0",
        "scipy==1.7.1",
    ],
)