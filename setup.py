#!/usr/bin/env python
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
import os
import os.path

import sys


setup(name="dicomparser",
      packages = find_packages(),
      include_package_data = True,
      version="0.1",
      zip_safe = False, # want users to be able to see included examples,tests
      description="Parse dicom file and return as a dictionary",
      author="Hrishikesh K B",
      author_email="hrishi.kb@gmail.com",
      url="https://gitlab.com/stultus/dicom-parser/",
      license = "LICENCE.txt",
      keywords = "dicom python medicalimaging",
      classifiers = [
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries",
        ],
      long_description = open('README.txt').read(),
      install_requires=["pydicom >= 0.9.7"]
     )
