#!/usr/bin/env python
import os
import sys
from setuptools import setup
import glob

requirements = ["pyyaml",
                "nose>=1.3.7",
                "future-fstrings",
                "omegaconf",
                "click",
                "pydantic",
                "ruamel.yaml",
                "pytest",
                ],

PACKAGE_NAME = "scabha"

__version__ = "0.6.0"

setup(name=PACKAGE_NAME,
      version=__version__,
      description="Onboard services for passengers of Stimela (https://github.com/caracal-pipeline/stimela2) cabs",
      author="Oleg Smirnov & RATT",
      author_email="osmirnov@gmail.com",
      url="https://github.com/caracal-pipeline/scabha2",
      packages=["scabha"],
      package_data={"scabha": []},
      install_requires=requirements,
      scripts=[],
      classifiers=[],
      )
