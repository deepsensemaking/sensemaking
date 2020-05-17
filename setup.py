#!/usr/bin/env python
# -*- coding: utf-8 -*


from setuptools import setup, find_namespace_packages
setup(
    name             = "sensemaking",
    packages         = find_namespace_packages(where="src"),
    python_requires  = ">3.6",
    version          = "0.1.2020.05.16.1",
    url              = "https://github.com/deepsensemaking/sensemaking",
    download_url     = "https://github.com/deepsensemaking/sensemaking/releases/download/v0.1.2020.05.16.1/sensemaking-0.1.2020.5.16.1-py3-none-any.whl",
    description      = "DeepSenseMaking (dsm) Tools",
    keywords         = [
        "sensemaking",
        "nlp",
        "ml",
        "ai",
    ],
    install_requires = [
        "argparse",
        "pandas",
        "numpy",
        "scipy",
    ],
    package_dir      = {"": "src"},
    license          = "GNU General Public License v3.0",
    scripts          = ["src/bin/sensemaking-cli"],
    author           = "DeepSenseMaking Developes",
    author_email     = "sensemaking@gmail.com",
    # long_description=open("README.txt").read(),
    # We will also need a readme eventually (there is going to be a warning)
)
